import boto3 
from config.config import  GLUE_DATABASE

glue = boto3.client("glue")

def list_tables():
    response = glue.get_tables(
        DatabaseName = GLUE_DATABASE
    )

    for table in response["TableList"]:
        print(table["Name"])


if __name__=="__main":
    list_tables()


