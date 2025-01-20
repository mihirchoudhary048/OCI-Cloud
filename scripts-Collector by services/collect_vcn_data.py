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

def get_vcns_for_compartment(compartment_id, region):
    """Retrieve all VCN details for a given compartment in a specific region."""
    command = f"oci network vcn list --compartment-id {compartment_id} --region {region} --all --output json"
    return run_oci_command(command)

def save_json_to_file(directory, filename, data):
    """Save data to a JSON file."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filepath}")

def collect_vcn_data(output_dir):
    regions = get_all_regions()
    if not regions:
        print("Failed to retrieve regions.")
        return

    compartments = get_all_compartments()
    if not compartments:
        print("Failed to retrieve compartments.")
        return

    for region in regions:
        for compartment in compartments.get('data', []):
            compartment_id = compartment['id']
            compartment_name = compartment['name']
            print(f"Processing VCNs for compartment: {compartment_name} (ID: {compartment_id}) in region: {region}")

            vcns = get_vcns_for_compartment(compartment_id, region)
            if vcns:
                save_json_to_file(output_dir, f"{region}_{compartment_name}_vcns.json", vcns)
            else:
                print(f"No VCNs found for compartment: {compartment_name} in region: {region}")

if __name__ == "__main__":
    output_directory = sys.argv[1]
    collect_vcn_data(output_directory)

