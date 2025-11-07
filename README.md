# WebTableScraper

🧮 Scrapes tables from websites (like Wikipedia) and saves them as CSV files.

## Features
- Extract tables from any HTML page
- Clean data and remove reference tags
- Save results in CSV format
- Two versions: Basic & Standard

## Versions
- **basic_v1.py** → Simple working version
- **standard_v2.py** → Improved: multi-table support, cleaner data, better structure

## Requirements
- Python 3.x
- Libraries:
  ''' bash
pip install requests beautifulsoup4
Folder Structure

WebTableScraper/
├── basic_v1.py
├── standard_v2.py
├── output/
│   └── sample_output.csv
├── examples/
│   └── table_preview.txt
└── docs/
    └── usage_guide.md

Usage

1. Run Basic Version:



python basic_v1.py

2. Run Standard Version:



python standard_v2.py

Example

Input (from a table):

Country	Population

Kalid	6
Mamad	7


Output (sample_output.csv):

Country,Population
Kalid,6
Mamad,7

Notes

Standard version supports multiple tables per page

Removes reference tags like [1], [2], etc.

Always check output/ folder for saved CSVs


---
