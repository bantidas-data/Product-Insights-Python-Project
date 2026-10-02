#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scraper import Scraper
from processor import DataProcessor
from analyzer import AnalyzerVisualizer
from db_handler import DatabaseHandler


# In[2]:


class Scraper:

    def __init__(self):
        self.base_url = ...

    def fetch_page(self):
        ...


# In[3]:


class Scraper:

    def __init__(self):
        ...

    def fetch_page(self, url):
        ...

    def parse_product(self, product):
        ...

    def parse_page(self, html):
        ...

    def scrape_all(self):
        ...


# In[4]:


df["Product ID"] = df["Product ID"].astype(str).str.strip()


# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv("data/raw_products.csv")


# In[7]:


df = pd.read_csv("../data/raw_products.csv")


# In[8]:


import os

print(os.getcwd())


# In[9]:


os.listdir()


# In[10]:


df = pd.read_csv("data/raw_products.csv")


# In[11]:


import os

print(os.path.exists("../data/raw_products.csv"))


# In[12]:


print(os.listdir("../"))
print(os.listdir("../data"))


# In[13]:


import os

print("Current folder:")
print(os.getcwd())

print("\nFiles/folders in current folder:")
print(os.listdir())


# In[14]:


import pandas as pd

df = pd.read_csv("data/raw_products.csv")

print(df.head())
print(df.shape)


# In[15]:


df["Product ID"] = df["Product ID"].astype(str).str.strip()


# In[16]:


print(os.getcwd())
print(os.listdir())


# In[18]:


import os

matches = []

for root, dirs, files in os.walk(os.getcwd()):
    if "raw_products.csv" in files:
        matches.append(os.path.join(root, "raw_products.csv"))

print("Found files:")
for path in matches:
    print(path)


# In[19]:


import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Desktop\Product_Insights_Project\data\raw_products.csv")

print(df.head())
print(df.shape)


# In[20]:


print(os.getcwd())


# In[ ]:




