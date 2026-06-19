import boto3

from config.config import (
    ATHENA_DATABASE,
    ATHENA_OUTPUT
)

athena = boto3.client(
    "athena"
)

def execute_query(query):

    response = athena.start_query_execution(

        QueryString=query,

        QueryExecutionContext={
            "Database":
            ATHENA_DATABASE
        },

        ResultConfiguration={
            "OutputLocation":
            ATHENA_OUTPUT
        }
    )

    return response[
        "QueryExecutionId"
    ]