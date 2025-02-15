GitHub README.md (Updated for All Scripts)
Now, here’s an updated README.md for all your scripts so that your GitHub repo is fully documented.

📜 Create/Update README.md in Your GitHub Repo
md
Copy
Edit
# AWS Inventory Automation Scripts 🚀

A collection of Python scripts using **Boto3** to **automate AWS resource collection** and generate **Excel reports**.

## 📌 Included Scripts & Features
| Script Name | Description |
|------------|-------------|
| `aws_list_s3.py` | Lists all **S3 buckets** and exports to Excel |
| `aws_inventory_report.py` | Collects **basic AWS inventory** (EC2, S3, RDS, IAM) and saves as Excel |
| `aws_inventory_advance_report.py` | **Full AWS tenancy report** (EC2, VPCs, Security Groups, S3, RDS, IAM, Route 53, CloudFront, Cost Report) |
| `aws_inventory_report.xlsx` | Sample **Basic AWS Inventory Report** |
| `aws_inventory_advance_report.xlsx` | Sample **Advanced AWS Inventory Report** |
| `s3_buckets_list.xlsx` | Sample **S3 Bucket List Report** |

---

## 🔧 **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mihirchoudhary048/AWS.git
cd AWS
2️⃣ Install Dependencies
bash
Copy
Edit
pip install boto3 pandas openpyxl
3️⃣ Run Any Script
👉 List all S3 Buckets

bash
Copy
Edit
python aws_list_s3.py
👉 Run the AWS Inventory Script (Basic)

bash
Copy
Edit
python aws_inventory_report.py
👉 Run the Advanced AWS Inventory Script

bash
Copy
Edit
python aws_inventory_advance_report.py
4️⃣ Download Reports from AWS CloudShell
📌 If using AWS CloudShell, download the generated Excel reports:

Click on Actions → Download File
Enter the filename, e.g., aws_inventory_report.xlsx
Save the file locally
📊 Sample Excel Report
Instance ID	Type	State	Public IP	Private IP	Launch Time
i-12345678	t2.micro	running	52.1.1.1	192.168.1.1	2024-02-15
📌 The Excel file includes separate sheets for EC2, S3, VPCs, Security Groups, IAM, Route 53, and more! 🚀

