import boto3

glue = boto3.client("glue")

response = glue.get_job_runs(
    JobName="sales-etl-job",
    MaxResults=1
)

print(response["JobRuns"][0]["ErrorMessage"])