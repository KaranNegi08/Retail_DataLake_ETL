import boto3

from config.config import (
    GLUE_JOB,
    GLUE_ROLE,
    BUCKET_NAME
)

glue_client = boto3.client(
    "glue"
)

def create_job():

    try:

        response = glue_client.create_job(

            Name=GLUE_JOB,

            Role=GLUE_ROLE,

            GlueVersion="4.0",

            WorkerType="G.1X",

            NumberOfWorkers=2,

            Command={
                "Name": "glueetl",

                "ScriptLocation":
                f"s3://{BUCKET_NAME}/scripts/sales_etl_job.py",

                "PythonVersion": "3"
            },

            DefaultArguments={
                "--job-language": "python",
                "--enable-metrics": "true",
                "--enable-continuous-cloudwatch-log": "true"
            }

        )

        print(
            f"Glue Job Created: {GLUE_JOB}"
        )

        return response

    except glue_client.exceptions.AlreadyExistsException:

        print(
            f"{GLUE_JOB} already exists"
        )

    except Exception as e:

        print(
            f"Error creating job: {e}"
        )