import os

from utils.s3_helper import s3_client
from config.config import BUCKET_NAME

LOCAL_PARQUET_DIR = "data/output/processed_sales"

for root, dirs, files in os.walk(LOCAL_PARQUET_DIR):

    for file in files:

        full_path = os.path.join(root, file)

        s3_key = full_path.replace(
            "\\",
            "/"
        )

        s3_client.upload_file(
            full_path,
            BUCKET_NAME,
            f"processed/sales/{s3_key}"
        )

print("Parquet Uploaded")