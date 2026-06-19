import boto3

from config.config import BUCKET_NAME

s3 = boto3.client("s3")

def upload_glue_script():

    s3.upload_file(
        "glue_jobs/sales_etl_job.py",
        BUCKET_NAME,
        "scripts/sales_etl_job.py"
    )

    print("Glue Script Uploaded")