#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyodbc
import pandas as pd


# In[2]:


df = pd.read_csv("data/clean_products.csv")

df.head()


# In[4]:


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-V9S50FT\\SQLEXPRESS;"
    "DATABASE= ProductDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

print("Connected Successfully!")


# In[5]:


import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-V9S50FT\\SQLEXPRESS;"
    "DATABASE=ProductDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

print("Connected Successfully!")


# In[6]:


cursor.execute("""
IF OBJECT_ID('Products', 'U') IS NULL
CREATE TABLE Products(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(255),
    Price FLOAT,
    Category NVARCHAR(100),
    ProductURL NVARCHAR(MAX)
)
""")

conn.commit()

print("Table Created Successfully!")


# In[7]:


for index, row in df.iterrows():
    cursor.execute("""
    INSERT INTO Products(ProductName, Price, Category, ProductURL)
    VALUES (?, ?, ?, ?)
    """,
    row["Product Name"],
    row["Price"],
    row["Category"],
    row["Product URL"])

conn.commit()

print("Data Inserted Successfully!")


# In[8]:


cursor.execute("SELECT TOP 10 * FROM Products")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[9]:


cursor.close()
conn.close()

print("Database Connection Closed.")


# In[ ]:




