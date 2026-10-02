#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:

    def __init__(self):
        self.base_url = "https://scrapeme.live/shop"
        self.products = []

    def fetch_page(self, url):

        response = requests.get(
            url,
            timeout=15
        )

        response.raise_for_status()

        return response.text

    def parse_product(self, product):

        name_tag = product.find(
            "h2",
            class_="woocommerce-loop-product__title"
        )

        price_tag = product.find(
            "span",
            class_="price"
        )

        link_tag = product.find("a")

        image_tag = product.find("img")

        name = (
            name_tag.get_text(strip=True)
            if name_tag else ""
        )

        price = (
            price_tag.get_text(strip=True)
            if price_tag else "£0"
        )

        product_url = (
            link_tag.get("href")
            if link_tag else ""
        )

        image_url = (
            image_tag.get("src")
            if image_tag else ""
        )

        product_id = (
            product_url.rstrip("/")
            .split("/")[-1]
        )

        return {
            "Product ID": product_id,
            "Product Name": name,
            "Category": "Unknown",
            "Price": price,
            "Discount": 0,
            "Rating": 0,
            "Number of Reviews": 0,
            "Availability": "In Stock",
            "Product URL": product_url,
            "Image URL": image_url
        }

    def parse_page(self, html):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        products = soup.find_all(
            "li",
            class_="product"
        )

        page_products = []

        for product in products:

            product_data = self.parse_product(
                product
            )

            page_products.append(
                product_data
            )

        return page_products

    def scrape_all(self, max_pages=7):

        self.products = []

        for page in range(1, max_pages + 1):

            if page == 1:
                url = f"{self.base_url}/"
            else:
                url = (
                    f"{self.base_url}/"
                    f"page/{page}/"
                )

            print(f"Scraping page {page}...")

            html = self.fetch_page(url)

            page_products = self.parse_page(
                html
            )

            self.products.extend(
                page_products
            )

            print(
                "Products collected:",
                len(self.products)
            )

        return self.products

    def save_to_csv(
        self,
        filename="data/raw_products.csv"
    ):

        df = pd.DataFrame(
            self.products
        )

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Saved {len(df)} products "
            f"to {filename}"
        )


if __name__ == "__main__":

    scraper = Scraper()

    scraper.scrape_all()

    scraper.save_to_csv()


# In[ ]:




