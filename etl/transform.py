from pyspark.sql.functions import (col,year,month,to_date)

def transform(df):
    print("Initial Record Count")
    print(df.count())

    # Remove duplicates
    df = df.dropDuplicates()
    #Remove Duplicates
    df = df.filter(col("amount").isNotNull())

    #Cast Amount
    df= df.withColumn(
        "amount",col("amount").cast("double")

    )

    #Convert Date
    df=df.withColumn(
        "order_date", to_date("order_date")
    )

    # Partition Columns

    df = df.withColumn(
        "year",
        year("order_date")
    )

    df = df.withColumn(
        "month",
        month("order_date")
    )

    return df