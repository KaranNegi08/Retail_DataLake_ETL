from config.config import PROCESSED_PATH

def load(df):
    try:

        # df.write.mode("overwrite").partitionBy(
        #     "year","month"
        # ).parquet(
        #     PROCESSED_PATH
        # )

        df.write \
        .mode("overwrite") \
        .partitionBy("year","month") \
        .parquet(
            "data/output/processed_sales"
        )
        print("Parquet Written Successfully...")
    except Exception as e:
        print(e)

    