
---

# Table Extractor – Basic Version

## Overview
**Table Extractor (Basic Version)** is a simple Python script that extracts the **first HTML table** from a website and saves it as a CSV file.  
This version is perfect for beginners or clients who need **quick table extraction** from a single webpage.

---

## Features
- ✅ Extracts the **first table** from any webpage containing HTML tables.  
- ✅ Saves the table as a **CSV file** (`extracted_table.csv`).  
- ✅ Checks if the **website URL is valid** and reachable before extraction.  
- ✅ Handles **basic errors** gracefully if extraction fails.  
- ✅ Beginner-friendly with **clear step-by-step comments**.

---

## Requirements
- Python 3.x  
- Python packages:  
  ```bash
  pip install pandas requests


---

How to Use

1. Open the script: table_extractor_basic.py.


2. Run the script:

python table_extractor_basic.py


3. Enter the website URL when prompted (must include https://):

Enter link website: https://www.contextures.com/xlSampleData01.html


4. The script will:

Check if the URL is valid.

Extract the first table.

Save it as extracted_table.csv in the same folder.



5. If successful, you will see:

✅ URL is valid and reachable
✅ Table extracted and saved as 'extracted_table.csv'




---

Sample Output

The extracted CSV file will look like this (first few rows):

OrderID	Product	Quantity	Price

10248	Pencil	12	1.50
10249	Pen	20	2.00


The table content depends on the website.


---

Known Limitations (Basic Version)

Extracts only the first table from the website.

Cannot extract multiple tables or custom CSV names.

No optional table preview before saving.

Minimal logging for errors (only console messages).



---

Upgrading to Standard Version

To make this script Standard Version (70% delivery), the following improvements can be added:

1. Multiple Tables Extraction: Extract and save all tables on the webpage.


2. Custom CSV Names: Allow users to set a base name for CSV files.


3. Table Preview: Display the first few rows of each table before saving.


4. Error Logging: Save errors and extraction info in a log file (extracted_log.txt).


5. Client-Friendly UX: Better prompts, validation, and dynamic file handling.




---

Why This Script is Useful

Quick and simple solution for table extraction.

Perfect for freelance clients who need data from websites in CSV format.

Beginner-friendly for learning Python, pandas, and web scraping basics.



---

Credits

Developed by KalidCodeHub

Focus: Python automation, data extraction, and client-ready scripts.

Website: KalidCodeHub Portfolio



---

License

This project is free to use, modify, and share for learning or freelance purposes.

