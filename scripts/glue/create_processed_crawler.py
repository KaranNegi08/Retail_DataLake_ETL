import boto3

from config.config import (
    PROCESSED_CRAWLER,
    GLUE_DATABASE,
    GLUE_ROLE,
    BUCKET_NAME
)

glue = boto3.client("glue")

def create_processed_crawler():

    try:

        glue.create_crawler(

            Name=PROCESSED_CRAWLER,

            Role=GLUE_ROLE,

            DatabaseName=GLUE_DATABASE,

            TablePrefix="processed_",

            Targets={
                "S3Targets": [
                    {
                        "Path":
                        f"s3://{BUCKET_NAME}/processed/sales/"
                    }
                ]
            }
        )

        print(
            "Processed Crawler Created"
        )

    except glue.exceptions.AlreadyExistsException:

        print(
            "Processed Crawler Already Exists"
        )