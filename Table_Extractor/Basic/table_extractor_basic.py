# ==============================
# Basic Version: Extract Table from Website to CSV
# Description: Reads first HTML table from a website and saves as CSV
# ==============================

import pandas as pd
import requests

# Step 1: Set website URL that contains the table
url = input("Enter link website: ").strip()

# Step 2: check link 
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ URL is valid and reachable")
    else:
        print("❌ URL returned status code:", response.status_code)
        exit()
except Exception as e:
    print("❌ Failed to reach URL:", e)
    exit()
    
#read tables 
try:
    tables = pd.read_html(url)
    table = tables[0]
    table.to_csv("extracted_table.csv", index=False)
    print("✅ Table extracted and saved as 'extracted_table.csv'")
except Exception as e:
    print("❌ Failed to extract table:", e)


