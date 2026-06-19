import time

import boto3

from config.config import (
    GLUE_JOB
)

glue_client = boto3.client(
    "glue"
)

def check_job_status(job_run_id):

    while True:

        response = glue_client.get_job_run(

            JobName=GLUE_JOB,

            RunId=job_run_id
        )

        status = response[
            "JobRun"
        ][
            "JobRunState"
        ]

        print(
            f"Current Status: {status}"
        )

        if status in [

            "SUCCEEDED",

            "FAILED",

            "STOPPED",

            "TIMEOUT"

        ]:

            break

        time.sleep(30)

    return status