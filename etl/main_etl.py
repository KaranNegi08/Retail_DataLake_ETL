from etl.extract import extract
from etl.load import load
from etl.transform import transform
from config.config import RAW_PATH


def etl_pipeline():
    spark = extract()

    #Read CSV from s3
    # df = spark.read.csv(
    #     RAW_PATH, header=True, inferSchema = True
    # )

    df = spark.read.csv(
    "data/input/sales_data.csv",
    header=True,
    inferSchema=True
    )
    print("Raw Data")
    df.show()

    #Transform

    clean_df = transform(df)
    print("Cleaned Data.")

    clean_df.show()

    #Load
    load(clean_df)

    spark.stop()

if __name__=="__main__":
    etl_pipeline()