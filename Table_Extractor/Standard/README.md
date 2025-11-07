
---

# Table Extractor – Standard Version

### Overview

Table Extractor is a Python script to extract HTML tables from any website and save them as CSV files.

This Standard Version includes:

Extract multiple tables from a website

Validate URL and network before extraction

Optional preview of tables before saving

Custom CSV file naming

Error logging for troubleshooting


It’s beginner-friendly, client-ready, and modular—easy to upgrade to a Pro version with extra features.


---

## Features

Extract all tables found on a webpage and save as numbered CSV files

Option to enter a custom CSV base name

Preview first 5 rows of each table before saving

Validate website URL and network connection

Log errors in extracted_log.txt

Step-by-step prompts for ease of use

Ready for future upgrades like Excel export or folder management



---

## Requirements

Python 3.8+

Libraries: pandas, requests, lxml


pip install pandas requests lxml

Internet connection for online table extraction



---

### How to Use

1. Run the script:



python table_extractor_standard.py

2. Enter the website URL (must start with https:// or http://)


3. Enter a custom CSV base name (optional)


4. Choose whether to preview tables (yes/no)


5. Extracted CSV files are saved in the script folder; errors are logged in extracted_log.txt




---

Example

Enter website link (with https://): https://www.contextures.com/xlSampleData01.html
Enter base CSV file name (default 'extracted_table.csv'): mydata
Do you want to preview tables? (yes/no): yes

✅ Found 1 table(s) on the website.
Table 1 preview:
   OrderDate   Region     Rep      Item  Units  UnitCost  Total
0  1/6/2020   East      Jones    Pencil    95      1.99  189.05
1  1/23/2020  Central   Kivell   Binder    50     19.99  999.50
...
✅ Table 1 saved as 'mydata_table1.csv'


---

File Structure

Table_Extractor_Standard/
│
├── table_extractor_standard.py    # Main script
├── extracted_log.txt              # Error log
├── sample_output/                 # Optional sample CSV files
│   └── mydata_table1.csv
└── README.md                      # Project documentation


---

Error Handling

Network issues: script checks URL reachability

No tables found: shows message and logs error

Other exceptions: logged in extracted_log.txt



---

### Upgrade Notes

Automatic folder creation for multiple CSVs

Export tables to Excel (.xlsx)

Custom CSV names for each table

Batch processing or scheduled scraping

GUI interface for clients



---

Tips for Clients

Ensure the website contains HTML tables

Use a valid and reachable URL

Preview option helps verify table content before saving



---

#### Author / Developer

KalidCodeHub
Freelance Python Developer
Specializes in automation, data extraction, and client-ready scripts
Portfolio: [GitHub Link]


