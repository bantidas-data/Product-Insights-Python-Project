# Product Insights Through Web Scraping, Analysis, and Database Integration

## Project Overview

This project demonstrates an end-to-end Python data analysis workflow.

The project collects product information from a public e-commerce website using web scraping, cleans and processes the data using Pandas and NumPy, performs analysis, creates visualizations, generates a summary report, and stores product data in a SQL Server database.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- NumPy
- Matplotlib
- Plotly
- PyODBC
- SQL Server

## Project Structure

```text
Product_Insights_Project/
│
├── README.md
├── scraper.py
├── processor.py
├── analyzer.py
├── db_handler.py
├── main.py
│
├── data/
│   ├── raw_products.csv
│   └── clean_products.csv
│
├── charts/
│   ├── average_price_by_category.png
│   ├── rating_histogram.png
│   └── price_vs_rating.html
│
├── reports/
│   └── analysis_summary.txt
│
└── ProductDB.bak


