import time
import boto3

glue = boto3.client("glue")

def crawler_status(crawler_name):

    while True:

        response = glue.get_crawler(
            Name=crawler_name
        )

        state = response[
            "Crawler"
        ][
            "State"
        ]

        print(
            f"{crawler_name}: {state}"
        )

        if state == "READY":

            return

        time.sleep(15)