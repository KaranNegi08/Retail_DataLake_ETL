from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.context import SparkContext

from pyspark.sql.functions import (
    col,
    year,
    month,
    to_date
)

sc = SparkContext()

glueContext = GlueContext(sc)

spark = glueContext.spark_session

job = Job(glueContext)

job.init("sales-etl-job", {})

dynamic_frame = (
    glueContext
    .create_dynamic_frame
    .from_catalog(
        database="sales_db",
        table_name="sales"
    )
)

df = dynamic_frame.toDF()

df = df.dropDuplicates()

df = df.filter(
    col("amount").isNotNull()
)

df = df.withColumn(
    "amount",
    col("amount").cast("double")
)

df = df.withColumn(
    "order_date",
    to_date("order_date")
)

df = df.withColumn(
    "year",
    year("order_date")
)

df = df.withColumn(
    "month",
    month("order_date")
)

(
    df.write
    .mode("overwrite")
    .partitionBy(
        "year",
        "month"
    )
    .parquet(
        "s3://retail-datalake-1/processed/sales/"
    )
)

job.commit()