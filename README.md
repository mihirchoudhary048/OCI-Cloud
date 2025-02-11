OCI Cloud Automation Scripts

This repository contains a collection of Python scripts for automating various tasks in Oracle Cloud Infrastructure (OCI). These scripts are designed to streamline cloud management, improve security, optimize costs, and ensure compliance with OCI best practices.

📌 Features

Orphan Resources Collector: Identifies and reports orphaned resources to optimize costs.

Policy Collector: Exports and analyzes OCI policies for governance and compliance.

Security List Collector: Collects OCI security configurations for auditing.

VCN Collector: Gathers Virtual Cloud Network (VCN) details for networking assessments.

CloudGuard Integration: Enhances security insights by integrating with OCI CloudGuard.

Comprehensive Resource Discovery: Collects all OCI resources for better visibility.

Automated Reports: Generates structured reports in JSON/CSV format for analysis.

📂 Folder Structure

├── OCI_Orphan_Resources_Collector       # Identifies unused resources
├── OCI_Policy_Collector                 # Extracts and audits OCI policies
├── OCI_Security_List                    # Collects security configurations
├── OCI_VCN_Collector                    # Retrieves Virtual Cloud Network details
├── OCI_all_resources_collector_with_CloudGuard # Collects all OCI resources with security insights
├── Output file                           # Stores execution results
├── Python scripts for OCI                # Collection of Python scripts for automation
├── scripts-Collector by services         # Categorized scripts for different OCI services
├── requirements.txt                      # Dependencies for running scripts
└── README.md                             # Documentation for the repository

🚀 Getting Started

Prerequisites

Ensure you have the following installed before running the scripts:

Python 3.x: Download from python.org

OCI CLI: Install using OCI CLI setup guide

OCI Python SDK: Install via pip

pip install oci

Authentication Setup:

Ensure you have an OCI config file at ~/.oci/config with required credentials.

Example config file:

[DEFAULT]
user=ocid1.user.oc1..xxxxx
fingerprint=xx:xx:xx:xx:xx:xx
key_file=/path/to/your/private/api_key.pem
tenancy=ocid1.tenancy.oc1..xxxxx
region=us-ashburn-1

🔧 Installation

Clone this repository and install dependencies:

git clone <repository_link>
cd <repo_directory>
pip install -r requirements.txt

📌 Usage

Each script is designed for a specific task in OCI. Below are examples of how to execute them.

Running the Orphan Resources Collector

python OCI_Orphan_Resources_Collector/orphan_collector.py --tenancy_id <your_tenancy_id>

Exporting OCI Policies

python OCI_Policy_Collector/policy_export.py --tenancy_id <your_tenancy_id>

Collecting Security List Details

python OCI_Security_List/security_audit.py --tenancy_id <your_tenancy_id>

Fetching VCN Information

python OCI_VCN_Collector/vcn_discovery.py --tenancy_id <your_tenancy_id>

Running All Resource Collector with CloudGuard

python OCI_all_resources_collector_with_CloudGuard/resource_collector.py --tenancy_id <your_tenancy_id>

📊 Output Formats

The scripts generate reports in multiple formats for easy analysis:

CSV: Structured data for Excel/Google Sheets.

JSON: Machine-readable structured format.

Log files: Debugging and execution logs.

🔒 Security Considerations

Ensure that API keys and sensitive credentials are securely stored.

Use OCI Vault for managing secrets if required.

Restrict IAM permissions to allow only necessary access.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing

We welcome contributions! If you'd like to improve the scripts or add new features:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to your branch (git push origin feature-branch).

Open a Pull Request.

📬 Contact

For any questions or issues, feel free to raise an Issue or contact:
📧 mihirchoudhary048@gmail.com

Happy Automating! 🚀
