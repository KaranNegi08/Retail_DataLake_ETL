import boto3

from config.config import (
    PROCESSED_CRAWLER
)

glue = boto3.client("glue")

def start_processed_crawler():

    glue.start_crawler(
        Name=PROCESSED_CRAWLER
    )

    print(
        "Processed Crawler Started"
    )