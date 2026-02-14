import pandas as pd
from ingestion_sqlite_db import ingest_db, get_connection
import logging
import os

db_path = r"data\inventory.db"
log_dir = r"data\logs"
log_file = os.path.join(log_dir, "get_vendor_summary.log")

logger = logging.getLogger("vendor_summary")
logger.setLevel(logging.DEBUG)

# Only add handler if it doesn't exist
if not logger.handlers:
    handler = logging.FileHandler(log_file, mode='a')
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.info("This should create get_vendor_summary.log")


def create_vendor_summary(conn):
    """
    This function merges different tables to get overall vendor summary
    and adds new columns in the resultant data
    """

    query = """
    WITH FreightSummary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS FreightCost 
        FROM vendor_invoice 
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.PurchasePrice,
            p.Description,
            pp.Volume,
            pp.Price AS ActualPrice,
            SUM(p.Quantity) AS TotalQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM purchases AS p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.PurchasePrice,
            p.Description,
            pp.Price,
            pp.Volume
    ),

    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Description,
        ps.Brand,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
       AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    """

    return pd.read_sql_query(query, conn)


def clean_data(df):
    """This function cleans and enriches the data"""

    # Clean string columns safely
    df['VendorName'] = df['VendorName'].fillna('').str.strip()
    df['Description'] = df['Description'].fillna('').str.strip()

    # Safe numeric conversion
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce').fillna(0)

    # Fill remaining nulls
    df.fillna(0, inplace=True)

    # KPI Calculations (safe from division by zero)
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars'].replace(0, 1)) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalQuantity'].replace(0, 1)
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars'].replace(0, 1)

    return df


if __name__ == '__main__':
    conn = get_connection(db_path)

    logger.info("Creating Vendor Summary Table...")
    summary_df = create_vendor_summary(conn)
    logger.info("\n%s", summary_df.head().to_string())

    logger.info("Cleaning Data...")
    clean_df = clean_data(summary_df)
    logger.info("\n%s", clean_df.head().to_string())

    logger.info("Ingesting Data into SQLite...")
    ingest_db(clean_df, "vendor_sales_summary", conn)

    conn.close()
    logger.info("Process Completed Successfully.")
