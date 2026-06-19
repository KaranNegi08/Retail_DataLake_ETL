import boto3 
from config.config import GLUE_DATABASE,GLUE_ROLE,CRAWLER_NAME,BUCKET_NAME

glue = boto3.client("glue")

def create_crawler():
    try:
        glue.create_crawler(
            Name = CRAWLER_NAME,
            Role = GLUE_ROLE,
            DatabaseName= GLUE_DATABASE,
            Targets={
            "S3Targets": [
                {
                    "Path":
                    f"s3://{BUCKET_NAME}/raw/sales/"
                }
            ]
        }
        )
        
        print(f"Crawler Created : {CRAWLER_NAME}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_crawler()