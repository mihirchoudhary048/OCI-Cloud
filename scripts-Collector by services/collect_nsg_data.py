import subprocess
import json
import os
import sys
from datetime import datetime

def run_oci_command(command):
    """Run an OCI CLI command and capture the JSON result."""
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        if not result.strip():
            print(f"Command produced no output: {command}")
            return None
        return json.loads(result)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return None

def get_all_regions():
    """Retrieve all regions the tenancy is subscribed to."""
    command = "oci iam region-subscription list --all --output json"
    result = run_oci_command(command)
    if result:
        return [region['region-name'] for region in result.get('data', [])]
    return []

def get_all_compartments():
    """Retrieve all compartments in the tenancy."""
    command = "oci iam compartment list --all --output json"
    return run_oci_command(command)

def get_nsgs_for_compartment(compartment_id, region):
    """Retrieve NSG details for a given compartment in a specific region."""
    command = f"oci network nsg list --compartment-id {compartment_id} --region {region} --all --output json"
    return run_oci_command(command)

def get_nsg_rules(nsg_id, region):
    """Retrieve rules for a given NSG."""
    command = f"oci network nsg rules list --nsg-id {nsg_id} --region {region} --all --output json"
    return run_oci_command(command)

def get_nsg_vnics(nsg_id, region):
    """Retrieve VNICs associated with a given NSG."""
    command = f"oci network nsg vnics list --nsg-id {nsg_id} --region {region} --all --output json"
    return run_oci_command(command)

def save_json_to_file(directory, filename, data):
    """Save data to a JSON file."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filepath}")

def collect_nsg_data(output_dir):
    regions = get_all_regions()
    if not regions:
        print("Failed to retrieve regions.")
        return

    compartments = get_all_compartments()
    if not compartments:
        print("Failed to retrieve compartments.")
        return

    for region in regions:
        print(f"Processing region: {region}")
        for compartment in compartments.get('data', []):
            compartment_id = compartment['id']
            compartment_name = compartment['name']
            print(f"  Processing compartment: {compartment_name} (ID: {compartment_id}) in region: {region}")

            # Create directory for NSG data
            region_dir = os.path.join(output_dir, f"nsg_data_{region}")
            os.makedirs(region_dir, exist_ok=True)

            # Fetch NSG details
            nsgs = get_nsgs_for_compartment(compartment_id, region)
            if nsgs:
                save_json_to_file(region_dir, f"{region}_{compartment_name}_nsg.json", nsgs)
                for nsg in nsgs.get('data', []):
                    nsg_id = nsg['id']
                    nsg_name = nsg['display-name']
                    print(f"    Collecting NSG rules and VNICs for NSG: {nsg_name} (ID: {nsg_id})")

                    # Fetch NSG rules
                    rules = get_nsg_rules(nsg_id, region)
                    if rules:
                        save_json_to_file(region_dir, f"nsg_{nsg_id}_rules.json", rules)

                    # Fetch NSG VNICs
                    vnics = get_nsg_vnics(nsg_id, region)
                    if vnics:
                        save_json_to_file(region_dir, f"nsg_{nsg_id}_vnics.json", vnics)
            else:
                print(f"No NSGs found in compartment: {compartment_name} for region: {region}")

if __name__ == "__main__":
    output_directory = sys.argv[1]  # Pass output directory as argument
    os.makedirs(output_directory, exist_ok=True)
    collect_nsg_data(output_directory)
    print("NSG data collection completed.")

