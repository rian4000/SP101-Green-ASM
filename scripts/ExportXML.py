import os
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp

output_dir = "../scans"
os.makedirs(output_dir, exist_ok=True)

connection = UnixSocketConnection(path="/run/gvmd/gvmd.sock")

with Gmp(connection) as gmp:
    gmp.authenticate("admin", "YOUR_ADMIN_PASSWORD")
    reports = gmp.get_reports(filter_string="rows=1 sort-reverse=date")
    report_id = reports.xpath("report/@id")[0]
    report_xml = gmp.get_report(
        report_id=report_id,
        report_format_id="a994b278-1f62-11e1-96ac-406186ea4fc5"  # XML format
    )
    with open(f"{output_dir}/latest_scan.xml", "w") as file:
        file.write(report_xml)
print("✅ Report exported as scans/latest_scan.xml")
