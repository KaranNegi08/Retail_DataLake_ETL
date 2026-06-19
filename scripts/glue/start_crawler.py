import boto3 
from config.config import CRAWLER_NAME

glue = boto3.client("glue")

def start_crawler():
    try:
        glue.start_crawler(
            Name=CRAWLER_NAME
        )
        print(f"Crawler Started...")
    except Exception as e:
        print(e)

if __name__=="__main__":
    start_crawler()


# What Happens Internally?

# Crawler starts.

# Glue Crawler
#       ↓
# Reads CSV
#       ↓
# Reads Header
#       ↓
# Samples Records
#       ↓
# Infers Datatypes
#       ↓
# Creates Metadata
#       ↓
# Stores in Catalog