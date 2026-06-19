import time
import boto3

athena = boto3.client(
    "athena"
)

def get_query_results(query_id):

    while True:

        response = athena.get_query_execution(
            QueryExecutionId=query_id
        )

        status = response[
            "QueryExecution"
        ][
            "Status"
        ][
            "State"
        ]

        print(
            f"Query Status: {status}"
        )

        if status == "SUCCEEDED":
            break

        time.sleep(5)

    results = athena.get_query_results(
        QueryExecutionId=query_id
    )

    return results