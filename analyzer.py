#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px


# In[2]:


df = pd.read_csv("data/clean_products.csv")

df.head()


# In[3]:


print(df.describe())


# In[4]:


category_count = df["Category"].value_counts()

print(category_count)


# In[5]:


average_price = df.groupby("Category")["Price"].mean()

print(average_price)


# In[6]:


most_expensive = df.loc[df["Price"].idxmax()]

print(most_expensive)


# In[7]:


cheapest = df.loc[df["Price"].idxmin()]

print(cheapest)


# In[8]:


category_count.plot(kind="bar")

plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")

plt.show()


# In[9]:


plt.hist(df["Price"], bins=10)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()


# In[11]:


fig = px.bar(
    df,
    x="Category",
    y="Price",
    color="Category",
    title="Category vs Price"
)

fig.show()


# # ABOVE I SHOW ERROE SO I DO THESE STEP AGAIN ......

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.io as pio


# In[2]:


print(pio.renderers.default)


# In[3]:


fig = px.bar(
    df,
    x="Category",
    y="Price",
    color="Category",
    title="Category vs Price"
)

fig.show()


# In[4]:


import plotly.io as pio

pio.renderers.default = "browser"


# In[5]:


fig.show()


# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv("data/clean_products.csv")


# In[8]:


df.head()


# In[9]:


import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"


# In[11]:


fig = px.bar(
    df,
    x="Category",
    y="Price",
    color="Category",
    title="Category vs Price"
)

fig.show()


# # FOR SAVING THESE CHART IN MY PROJECT FOLDER I RUN ANOTHER CODE

# # . Bar Chart (Matplotlib)

# In[12]:


import matplotlib.pyplot as plt

category_count = df["Category"].value_counts()

plt.figure(figsize=(8,5))
category_count.plot(kind="bar")

plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")

plt.tight_layout()

plt.savefig("charts/category_bar_chart.png")

plt.show()

print("Bar chart saved successfully!")


# # Histogram (Matplotlib)

# In[13]:


plt.figure(figsize=(8,5))

plt.hist(df["Price"], bins=10)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("charts/price_distribution.png")

plt.show()

print("Histogram saved successfully!")


# # Interactive Plotly Chart

# In[14]:


import plotly.express as px

fig = px.bar(
    df,
    x="Category",
    y="Price",
    color="Category",
    title="Category vs Price"
)

fig.write_html("charts/category_price_plotly.html")

print("Interactive Plotly chart saved successfully!")


# In[ ]:




