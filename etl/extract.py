from pyspark.sql import SparkSession

def extract():
    spark = SparkSession.builder.appName("Sales ETL").config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        ).getOrCreate()

    return spark