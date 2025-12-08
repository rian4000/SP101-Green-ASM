from google.cloud import storage
import os
from datetime import datetime

# --- CONFIGURATION ---
SERVICE_ACCOUNT = "/home/kali/SP101-Green-ASM/sp101asm-f6159cb0f692.json"
BUCKET_NAME = "sp101-asm-results"  # <-- replace with your GCS bucket name
UPLOAD_FILE = "/home/kali/SP101-Green-ASM/scans/normalized_results.csv"

def upload_to_gcs():
    if not os.path.exists(UPLOAD_FILE):
        print(f"⚠️ File not found: {UPLOAD_FILE}")
        return

    # Authenticate and connect
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    # Define destination path
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_blob = f"results/normalized_results_{timestamp}.csv"
    blob = bucket.blob(destination_blob)

    # Upload
    blob.upload_from_filename(UPLOAD_FILE)
    print(f"✅ Uploaded to gs://{BUCKET_NAME}/{destination_blob}")

if __name__ == "__main__":
    upload_to_gcs()
