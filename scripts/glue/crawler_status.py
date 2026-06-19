import time
import boto3

glue_client = boto3.client("glue")

def crawler_status(crawler_name):

    while True:

        response = glue_client.get_crawler(
            Name=crawler_name
        )

        state = response["Crawler"]["State"]

        print(
            f"{crawler_name} Status : {state}"
        )

        if state == "READY":
            print(
                f"{crawler_name} Completed Successfully"
            )
            return

        time.sleep(15)