from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp

# Connect to Greenbone Manager (OpenVAS)
connection = UnixSocketConnection(path="/run/gvmd/gvmd.sock")

with Gmp(connection) as gmp:
    gmp.authenticate("admin", "YOUR_ADMIN_PASSWORD")  # replace with your actual OpenVAS admin password

    # Create scan target
    target = gmp.create_target(name="Public Scan Target", hosts="scanme.nmap.org")
    print(f"Target created: {target}")

    # Full and Fast scan config ID
    scan_config_id = "daba56c8-73ec-11df-a475-002264764cea"

    # Create and start scan task
    task = gmp.create_task(
        name="ASM Demo Scan",
        config_id=scan_config_id,
        target_id=target,
    )
    print(f"Task created: {task}")

    gmp.start_task(task)
    print("Scan started successfully!")
