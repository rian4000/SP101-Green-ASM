import xml.etree.ElementTree as ET
import csv
import os

# Input and output paths
xml_path = os.path.expanduser('~/SP101-Green-ASM/scans/latest_scan.xml')
csv_path = os.path.expanduser('~/SP101-Green-ASM/scans/normalized_results.csv')

print(f" Parsing XML: {xml_path}")

# Parse the XML file
tree = ET.parse(xml_path)
root = tree.getroot()

# Create output CSV
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(['Host', 'Port', 'Severity', 'Name', 'Description'])

    for result in root.findall('.//result'):
        host = result.findtext('host', default='N/A')
        port = result.findtext('port', default='N/A')
        severity = result.findtext('threat', default='N/A')
        name = result.findtext('name', default='N/A')
        desc = result.findtext('description', default='N/A')

        # Clean up line breaks and extra quotes
        desc = desc.replace('\n', ' ').replace('\r', ' ').replace('"', "'")
        name = name.replace('"', "'")

        writer.writerow([host, port, severity, name, desc])

print(f" Normalized CSV saved at: {csv_path}")

