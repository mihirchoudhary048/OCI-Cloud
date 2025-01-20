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

def get_log_groups_for_compartment(compartment_id, region):
    """Retrieve all log group details for a given compartment in a specific region."""
    command = f"oci logging log-group list --compartment-id {compartment_id} --region {region} --all --output json"
    return run_oci_command(command)

def get_logs_for_log_group(log_group_id, region):
    """Retrieve all logs for a given log group in a specific region."""
    command = f"oci logging log list --log-group-id {log_group_id} --region {region} --all --output json"
    return run_oci_command(command)

def save_json_to_file(directory, filename, data):
    """Save data to a JSON file."""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filepath}")

def collect_log_group_data(output_dir):
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

            log_groups = get_log_groups_for_compartment(compartment_id, region)
            if log_groups:
                save_json_to_file(output_dir, f"{region}_{compartment_name}_log_groups.json", log_groups)

                for log_group in log_groups.get('data', []):
                    log_group_id = log_group.get('id')
                    logs = get_logs_for_log_group(log_group_id, region)
                    if logs:
                        save_json_to_file(output_dir, f"{region}_{compartment_name}_log_group_{log_group_id}_logs.json", logs)

if __name__ == "__main__":
    output_directory = sys.argv[1]
    collect_log_group_data(output_directory)

