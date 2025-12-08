from google.cloud import bigquery

client = bigquery.Client.from_service_account_json("../service_key.json")

dataset_id = "ASM_Dataset"
table_id = "Vulnerability_Results"
table_ref = client.dataset(dataset_id).table(table_id)

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

with open("../scans/normalized_results.csv", "rb") as f:
    job = client.load_table_from_file(f, table_ref, job_config=job_config)

job.result()
print(" Data uploaded to BigQuery successfully!")
