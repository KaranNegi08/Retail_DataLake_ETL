from utils.s3_helper import s3_client
from config.config import BUCKET_NAME

def download_file():

    s3_client.download_file(
        BUCKET_NAME,
        "raw/sales/sales_data.csv",
        "data/input/sales_data.csv"
    )

    print("Downloaded Successfully")