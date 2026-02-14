import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging setup
logging.basicConfig(
    filename=r"D:logs\ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# MySQL engine
engine = create_engine("mysql+pymysql://root:<PASSWORD>@localhost/inventory_db")

data_path = r"\data"


def ingest_db(df, table_name, engine):
    """This function ingests dataframe into database table"""
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )


def load_raw_data():
    """This function loads CSVs as dataframe and ingests into DB"""
    start_time = time.time()

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            try:
                file_path = os.path.join(data_path, file)
                df = pd.read_csv(file_path)

                table_name = file.replace(".csv", "").lower()

                logging.info(f"Ingesting {file} into table {table_name}")
                ingest_db(df, table_name, engine)

            except Exception as e:
                logging.error(f"Error processing {file}: {e}")

    end_time = time.time()
    total_time = (end_time - start_time) / 60

    logging.info("--------- Ingestion completed -------")
    logging.info(f"Total time taken: {total_time:.2f} minutes")


if __name__ == '__main__':
    load_raw_data()