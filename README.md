# Product Insights Analysis Using Python

## 📌 Project Overview

This project is an end-to-end Python data analysis project that demonstrates how product data can be collected, cleaned, analyzed, visualized, and stored in a SQL Server database.

The project uses web scraping to collect product information, processes the data using Python, performs exploratory analysis, creates visualizations, generates an analysis summary, and integrates the final data with SQL Server.

## 🎯 Project Objectives

- Collect product information using web scraping
- Clean and preprocess raw product data
- Perform product and category-level analysis
- Analyze product prices and ratings
- Create meaningful data visualizations
- Generate an analysis summary
- Store processed product data in SQL Server
- Demonstrate an end-to-end Python data analytics workflow

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Requests
- BeautifulSoup
- Matplotlib
- Plotly
- PyODBC
- SQL Server

## 📂 Project Structure

```text
Product-Insights-Python-Project/
│
├── analyzer.py
├── db_handler.py
├── main.py
├── processor.py
├── scraper.py
│
├── data/
│   ├── raw_products.csv
│   └── clean_products.csv
│
├── charts/
│   ├── category_bar_chart.png
│   ├── price_distribution.png
│   └── category_price_plotly.html
│
├── analysis_summary.txt
├── README.md
└── .gitignore
