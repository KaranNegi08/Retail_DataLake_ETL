from scripts.s3.create_bucket import create_bucket
from scripts.s3.create_folder import create_folder
from scripts.s3.upload_file import upload_file
from scripts.s3.upload_glue_script import upload_glue_script
from config.config import RAW_PREFIX
from scripts.glue.create_database import create_database

from scripts.glue.create_crawler import (
    create_crawler
)

from scripts.glue.start_crawler import (
    start_crawler
)

from scripts.glue.crawler_status import (
    crawler_status
)

from scripts.glue.create_job import (
    create_job
)

from scripts.glue.start_job import (
    start_job
)

from scripts.glue.check_job_status import (
    check_job_status
)
from scripts.glue.create_processed_crawler import (
    create_processed_crawler
)

from scripts.glue.start_processed_crawler import (
    start_processed_crawler
)

from scripts.glue.check_crawler_status import (
    crawler_status
)

from scripts.athena.execute_query import (
    execute_query
)

from scripts.athena.get_query_results import (
    get_query_results
)

from config.config import (
    PROCESSED_CRAWLER
)

# from scripts.glue.create_processed_crawler import (
#     create_processed_crawler
# )

# from scripts.glue.start_processed_crawler import (
#     start_processed_crawler
# )

from config.config import (
    RAW_CRAWLER
)


def main():

    print("\n" + "=" * 60)
    print("PHASE 1 : S3 DATA LAKE SETUP")
    print("=" * 60)

    create_bucket()

    create_folder()

    upload_file("data/input/sales_data.csv",RAW_PREFIX+"sales_data.csv")

    upload_glue_script()

    print("\nS3 Setup Completed")

    print("\n" + "=" * 60)
    print("PHASE 2 : GLUE DATABASE & RAW CRAWLER")
    print("=" * 60)

    # create_database()

    create_crawler()

    start_crawler()

    print("\nWaiting for Raw Crawler...")

    crawler_status(RAW_CRAWLER)

    print("\nRaw Catalog Ready")

    print("\n" + "=" * 60)
    print("PHASE 3 : GLUE ETL")
    print("=" * 60)

    create_job()

    job_run_id = start_job()

    if job_run_id:

        final_status = check_job_status(
            job_run_id
        )

        if final_status != "SUCCEEDED":

            print(
                f"\nGlue Job Failed : {final_status}"
            )

            return

    print("\nGlue ETL Completed")

    print("\n" + "=" * 60)
    
    print("\n" + "=" * 60)
    print("PHASE 4 : PROCESSED CRAWLER")
    print("=" * 60)

    create_processed_crawler()

    start_processed_crawler()

    crawler_status(
        PROCESSED_CRAWLER
    )

    print(
        "\nProcessed Catalog Ready"
    )

    print(
        "\nRunning Athena Query..."
    )

    query = """
    SELECT
        year,
        month,
        SUM(amount) AS revenue
    FROM processed_sales
    GROUP BY year, month
    ORDER BY year, month
    """

    query_id = execute_query(
        query
    )

    results = get_query_results(
        query_id
    )

    print(results)

    print(
        "\nPIPELINE COMPLETED"
    )


if __name__ == "__main__":
    main()
























# from scripts.s3.create_bucket import create_bucket
# from scripts.s3.create_folder import create_folder
# from scripts.s3.upload_file import upload_file
# from scripts.glue.create_database import create_database
# from scripts.glue.start_crawler import start_crawler
# from scripts.glue.create_crawler import create_crawler
# from scripts.glue.crawler_status import crawler_status
# from scripts.glue.list_tables import list_tables
# from scripts.glue.create_job import create_job
# from scripts.glue.start_job import start_job
# from scripts.glue.check_job_status import check_job_status
# from etl.download_file import download_file
# from config.config import RAW_PREFIX
# from etl.main_etl import etl_pipeline 
# def main():
#     # print("STEP 1")
#     # create_bucket()

#     # print("STEP 2")
#     # create_folder()

#     # print("STEP 3")
#     # upload_file("data/input/sales_data.csv",RAW_PREFIX+"sales_data.csv")

#     # print("Pipeline Completed...")
#     # create_database()
#     # create_crawler()
#     # start_crawler()
#     # crawler_status()
#     # list_tables()

#     create_job()
#     job_run_id = start_job()

#     check_job_status(
#         job_run_id
#     )

#     print("\n")
#     # etl_pipeline()
#     # download_file()
#     print("=" * 50)
#     print("PHASE 4 : PROCESSED CATALOG")
#     print("=" * 50)




# if __name__ == "__main__":
#     main()