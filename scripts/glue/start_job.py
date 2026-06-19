import boto3

from config.config import (
    GLUE_JOB
)

glue_client = boto3.client(
    "glue"
)

def start_job():

    try:

        response = glue_client.start_job_run(

            JobName=GLUE_JOB

        )

        job_run_id = response[
            "JobRunId"
        ]

        print(
            f"Job Started"
        )

        print(
            f"Run ID: {job_run_id}"
        )

        return job_run_id

    except Exception as e:

        print(
            f"Failed to start job: {e}"
        )