# ==============================
# Standard Version: Extract Table(s) from Website to CSV
# Description: Reads HTML tables from a website, optionally previews tables,
#              allows custom CSV names, validates URL/network, handles multiple tables.
# ==============================

import pandas as pd
import requests
import logging 
logging.basicConfig(filename="extracted_log.txt",level = logging.INFO,  format = "%(asctime)s -%(levelname)s -%(message)s")

# Step 1: Get website URL from user
url = input("Enter website link (with https://): ").strip()

# Step 2: Optional custom CSV base name
csv_base = input("Enter base CSV file name (default 'extracted_table.csv'): ").strip() or "extracted_table.csv"

# Step 3: Validate URL/network
try:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ URL returned status code {response.status_code}")
        logging.error(f"❌ URL returned status code {response.status_code}")
        exit()
except Exception as error:
    print("❌ Failed to reach URL:", error)
    logging.error("❌ Failed to reach URL:", error)
    exit()

# Step 4: Read tables
try:
    tables = pd.read_html(url)
    if len(tables) == 0:
        print("❌ No tables found on the website")
        logging.error("❌ No tables found on the website")
        exit()

    print(f"✅ Found {len(tables)} table(s) on the website.")

    # Step 5: Preview tables
    preview_choice = input("Do you want to preview tables? (yes/no): ").strip().lower()
    if preview_choice == "yes":
        for num, table in enumerate(tables, 1):
            print(f"\nTable {num} preview:")
            print(table.head())  # shows first 5 rows

    # Step 6: Save tables to CSV
    for num, table in enumerate(tables, 1):
        filename = f"{csv_base}_table{num}.csv"
        table.to_csv(filename, index=False)
        print(f"✅ Table {num} saved as '{filename}'")

except Exception as error:
    print("❌ Failed to extract tables:", error)
    logging.error("❌ Failed to extract tables:", error)