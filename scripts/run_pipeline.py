#!/usr/bin/env python3
import os
import subprocess

# Define paths
base_dir = os.path.expanduser("~/SP101-Green-ASM")
scripts_dir = os.path.join(base_dir, "scripts")
scans_dir = os.path.join(base_dir, "scans")
normalized_file = os.path.join(scans_dir, "normalized_results.csv")

print(" Starting ASM automation pipeline...\n")

# Step 1: Normalize the OpenVAS XML scan output
try:
    print(" Step 1: Normalizing scan results...")
    subprocess.run(["python3", f"{scripts_dir}/NormalizeResults.py"], check=True)
except subprocess.CalledProcessError:
    print(" Error: Failed to normalize results. Check XML files in scans/.")
    exit(1)

# Step 2: Upload the normalized CSV to Google Cloud
if os.path.exists(normalized_file):
    try:
        print("☁️ Step 2: Uploading to Google Cloud Storage...")
        subprocess.run(["python3", f"{scripts_dir}/UploadToGCS.py"], check=True)
    except subprocess.CalledProcessError:
        print(" Error: Upload failed. Check Google Cloud credentials or bucket name.")
        exit(1)
else:
    print(" Warning: Normalized results not found. Skipping upload step.")
    exit(1)

print("\n ASM Pipeline completed successfully!")
print(f" Uploaded file: {normalized_file}")

