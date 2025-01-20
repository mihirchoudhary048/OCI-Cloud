import os
import subprocess
from datetime import datetime

def create_directory(base_dir, sub_dir):
    """Create a sub-directory inside the base directory."""
    path = os.path.join(base_dir, sub_dir)
    os.makedirs(path, exist_ok=True)
    return path

def run_script(script_path, log_file, *args):
    """Run a Python script and log its output to a log file."""
    with open(log_file, 'w') as log:
        try:
            command = ['python', script_path] + list(args)
            subprocess.run(command, stdout=log, stderr=log, check=True)
        except subprocess.CalledProcessError as e:
            log.write(f"Script {script_path} failed with error: {e}\n")

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"NetworkDataCollection_{timestamp}"
    os.makedirs(base_dir, exist_ok=True)

    wrapper_log_file = os.path.join(base_dir, "wrapper_log.txt")

    with open(wrapper_log_file, 'w') as wrapper_log:
        wrapper_log.write(f"Wrapper script started at {timestamp}\n")

        # Run Subnet Data Collection Script
        subnet_dir = create_directory(base_dir, "subnet_details")
        subnet_log_file = os.path.join(subnet_dir, "subnet_log.txt")
        run_script("collect_subnet_data.py", subnet_log_file, subnet_dir)

        # Run Log Group and Metadata Collection Script
        flowlog_dir = create_directory(base_dir, "flowlog_details")
        flowlog_log_file = os.path.join(flowlog_dir, "flowlog_log.txt")
        run_script("collect_log_group_data.py", flowlog_log_file, flowlog_dir)

        # Run VCN Data Collection Script
        vcn_dir = create_directory(base_dir, "vcn_details")
        vcn_log_file = os.path.join(vcn_dir, "vcn_log.txt")
        run_script("collect_vcn_data.py", vcn_log_file, vcn_dir)

        # Run Subnet IP Utilization Collection Script
        sn_ip_utl_dir = create_directory(base_dir, "subnet_ip_utilization_details")
        sn_ip_utl_file = os.path.join(sn_ip_utl_dir, "subnet_ip_utilization_details.log")
        run_script("collect_subnet_ip_utilization_data.py", sn_ip_utl_file, sn_ip_utl_dir)

        # Run Route Table Data Collection Script
        route_table_dir = create_directory(base_dir, "route_table_details")
        route_table_log_file = os.path.join(route_table_dir, "route_table_log.txt")
        run_script("collect_route_table_data.py", route_table_log_file, route_table_dir)

        # Run LPG Data Collection Script
        lpg_dir = create_directory(base_dir, "lpg_data")
        lpg_log_file = os.path.join(lpg_dir, "lpg_log.txt")
        run_script("collect_lpg_data.py", lpg_log_file, lpg_dir)

        # Run NSG Data Collection Script
        nsg_dir = create_directory(base_dir, "nsg_data")
        nsg_log_file = os.path.join(nsg_dir, "nsg_log.txt")
        run_script("collect_nsg_data.py", nsg_log_file, nsg_dir)

        # Run Security List Data Collection Script
        security_list_dir = create_directory(base_dir, "security_list_data")
        security_list_log_file = os.path.join(security_list_dir, "security_list_log.txt")
        run_script("collect_security_list_data.py", security_list_log_file, security_list_dir)

        wrapper_log.write(f"Wrapper script completed. All data is in directory: {base_dir}\n")

if __name__ == "__main__":
    main()

