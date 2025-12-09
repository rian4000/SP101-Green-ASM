# SP101 Green ASM - Attack Surface Management System

## Introduction
The SP101 Green ASM project is a security automation framework that identifies and tracks vulnerabilities across computer systems.  
It was developed as a senior capstone project at Kennesaw State University to demonstrate how cybersecurity teams can automate the process of network scanning, vulnerability detection, and cloud-based reporting.

This project uses open-source security tools and Google Cloud services to simulate a real-world Attack Surface Management (ASM) platform.  
ASM is the continuous process of discovering, analyzing, and monitoring all systems and assets connected to a network to understand where an organization may be vulnerable.

## Purpose
The goal of this project is to:
1. Automatically scan a target network or system for open ports and vulnerabilities.
2. Normalize and organize the results into a structured data format.
3. Upload the findings to the cloud for analysis and visualization.

The system can be used as a foundation for organizations or researchers interested in building scalable vulnerability management and reporting tools.

## Tools and Technologies Used
- **OpenVAS (Greenbone Vulnerability Manager)**: Performs vulnerability scans on target systems.
- **Python**: Automates scanning, data parsing, and upload tasks.
- **Google Cloud Storage**: Stores vulnerability results in the cloud.
- **Google BigQuery (optional)**: Analyzes and queries vulnerability data.
- **Kali Linux**: The operating system used to run the scanning environment.

## How It Works
1. OpenVAS scans a target system or IP address range and exports the results as an XML file.
2. Python scripts process and clean the data into a CSV format.
3. The cleaned data is uploaded automatically to Google Cloud Storage.
4. (Optional) The data can then be imported into BigQuery or a dashboard for visualization.

This process creates a repeatable and automated pipeline for scanning and reporting vulnerabilities.

## Project Structure
SP101-Green-ASM/
  scripts/
    CreateOpenVASTargets.py      - Automates target creation in OpenVAS
    ExportXML.py                  - Exports scan results to XML
    NormalizeData.py              - Cleans raw scan output
    NormalizeResults.py           - Converts OpenVAS XML to CSV
    UploadToGCS.py                - Uploads results to Google Cloud Storage
    UploadToBigQuery.py           - Loads data into BigQuery (optional)
    run_pipeline.py               - Runs all steps automatically
  scans/
    latest_scan.xml               - Example OpenVAS scan result
    normalized_results.csv        - Output file generated after normalization
  README.md                       - Project documentation

## Requirements
To run this project you will need:
- A computer running Kali Linux (or any Debian-based system)
- Python 3.11 or newer
- OpenVAS installed and configured
- A Google Cloud account with access to:
  - Google Cloud Storage
  - BigQuery (optional)
- A service account key file from Google Cloud for authentication (JSON format)

## Installation

1. Clone the project
git clone https://github.com/
<your-username>/SP101-Green-ASM.git
cd SP101-Green-ASM

2. Set up a Python virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install required packages
pip install google-cloud-storage
4. Configure OpenVAS
sudo gvm-setup
sudo gvm-start
5. Export your scan results from OpenVAS as XML and move them into:
~/SP101-Green-ASM/scans/
## Running the Project

1. Run the normalization step:
python3 scripts/NormalizeResults.py
This will convert the XML scan results into a CSV file called normalized_results.csv.

2. Upload the results to Google Cloud Storage:
python3 scripts/UploadToGCS.py
3. (Optional) Load data into BigQuery for analysis:
python3 scripts/UploadToBigQuery.py
4. To run everything automatically:
python3 scripts/run_pipeline.py
## Expected Output
- A normalized CSV file containing hosts, ports, vulnerabilities, and severity levels.
- The CSV file uploaded to a Google Cloud Storage bucket.
- (Optional) Data available in BigQuery for queries and dashboards.

## Testing and Verification
- Verify that OpenVAS successfully runs a scan and generates an XML report.
- Confirm that NormalizeResults.py outputs a valid CSV file.
- Check Google Cloud Storage to ensure the file appears in the correct bucket.
- If using BigQuery, confirm that the table loads and data is queryable.

## Summary
The SP101 Green ASM system provides a working prototype for continuous vulnerability management.  
It automates the flow from network scanning to cloud data storage, helping organizations quickly visualize and understand their attack surface.

This project demonstrates how open-source tools and cloud technologies can be combined to create scalable cybersecurity solutions.

## Authors
Team Green ASM - Kennesaw State University  

Rian Chowdhury  

Jaimi Reed 

Alan Jose 

Julio Martinez
