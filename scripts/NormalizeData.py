import xml.etree.ElementTree as ET
import pandas as pd
import json
import os

scan_dir = "/home/kali/SP101-Green-ASM/scans"
output_file = "/home/kali/SP101-Green-ASM/scans/normalized_results.csv"

def parse_nmap_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for host in root.findall("host"):
        addr = host.find("address").attrib.get("addr")
        for port in host.findall(".//port"):
            port_id = port.attrib.get("portid")
            proto = port.attrib.get("protocol")
            service_elem = port.find("service")
            service = service_elem.attrib.get("name") if service_elem is not None else "unknown"
            state = port.find("state").attrib.get("state")
            data.append({
                "host": addr, "port": port_id, "protocol": proto,
                "service": service, "state": state
            })
    return pd.DataFrame(data)

def parse_openvas_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for result in root.findall(".//result"):
        host = result.findtext("host")
        port = result.findtext("port")
        name = result.findtext("name")
        severity = result.findtext("threat")
        cve = result.findtext("nvt/cve")
        data.append({
            "host": host, "port": port, "vulnerability": name,
            "cve": cve, "severity": severity
        })
    return pd.DataFrame(data)

dfs = []
for file in os.listdir(scan_dir):
    if file.endswith(".xml"):
        path = os.path.join(scan_dir, file)
        if "nmap" in file.lower():
            dfs.append(parse_nmap_xml(path))
        else:
            dfs.append(parse_openvas_xml(path))

if dfs:
    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv(output_file, index=False)
    print(f"✅ Normalized data saved to {output_file}")
else:
    print("⚠️ No XML files found in scans directory.")
