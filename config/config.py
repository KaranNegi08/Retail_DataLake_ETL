#AWS configuration

AWS_REGION= "eu-north-1"
BUCKET_NAME = "retail-datalake-1"

RAW_PREFIX = "raw/sales/"
PROCESSED_PREFIX = "processed/sales/"
CURATED_PREFIX = "curated/sales/"

ATHENA_OUTPUT = "athena-results/"
LOGS_PREFIX="logs/"

#PHASE 2
GLUE_DATABASE= "sales_db"
CRAWLER_NAME = "raw-sales-crawler"
GLUE_ROLE = "GlueServiceRole"

#PHASE 3
RAW_PATH = f"s3a://{BUCKET_NAME}/raw/sales/"
PROCESSED_PATH = f"s3a://{BUCKET_NAME}/processed/sales/"
GLUE_JOB="sales-etl-job"
RAW_TABLE = "sales"
RAW_CRAWLER = "raw-sales-crawler"

PROCESSED_CRAWLER = "processed-sales-crawler"

PROCESSED_TABLE = "processed_sales"

ATHENA_DATABASE = "sales_db"

ATHENA_OUTPUT = (
    f"s3://{BUCKET_NAME}/athena-results/"
)