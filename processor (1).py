#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import statistics
import math


class DataProcessor:

    def __init__(
        self,
        input_file="data/raw_products.csv"
    ):

        self.input_file = input_file
        self.df = None

    def load_data(self):

        self.df = pd.read_csv(
            self.input_file
        )

        return self.df

    def clean_data(self):

        # Remove duplicate rows
        self.df.drop_duplicates(
            inplace=True
        )

        # String cleaning
        self.df["Product ID"] = (
            self.df["Product ID"]
            .astype(str)
            .str.strip()
        )

        self.df["Product Name"] = (
            self.df["Product Name"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        self.df["Category"] = (
            self.df["Category"]
            .astype(str)
            .str.strip()
        )

        # Convert price
        self.df["Price"] = (
            self.df["Price"]
            .astype(str)
            .str.replace(
                "£",
                "",
                regex=False
            )
            .astype(float)
        )

        numeric_columns = [
            "Discount",
            "Rating",
            "Number of Reviews"
        ]

        for column in numeric_columns:

            self.df[column] = pd.to_numeric(
                self.df[column],
                errors="coerce"
            )

        self.df[numeric_columns] = (
            self.df[numeric_columns]
            .fillna(0)
        )

    def price_category(self, price):

        if price < 50:
            return "Low"

        elif price < 100:
            return "Medium"

        else:
            return "High"

    def rating_category(self, rating):

        if rating < 2:
            return "Poor"

        elif rating < 3:
            return "Average"

        elif rating < 4:
            return "Good"

        else:
            return "Excellent"

    def create_categories(self):

        self.df["Price Category"] = (
            self.df["Price"]
            .apply(self.price_category)
        )

        self.df["Rating Category"] = (
            self.df["Rating"]
            .apply(self.rating_category)
        )

    def create_list_comprehension(self):

        self.cleaned_names = [
            name.strip().title()
            for name in self.df["Product Name"]
        ]

    def create_tuples(self):

        self.product_tuples = [
            (
                row["Product ID"],
                row["Product Name"],
                row["Category"],
                row["Price"],
                row["Rating"]
            )
            for _, row in self.df.iterrows()
        ]

    def create_dictionaries(self):

        self.product_dictionary = {
            row["Product ID"]: (
                row["Product Name"],
                row["Category"],
                row["Price"],
                row["Rating"]
            )
            for _, row in self.df.iterrows()
        }

        self.category_count = (
            self.df["Category"]
            .value_counts()
            .to_dict()
        )

        self.category_prices = (
            self.df.groupby("Category")["Price"]
            .apply(list)
            .to_dict()
        )

    def create_numpy_features(self):

        prices = self.df[
            "Price"
        ].to_numpy()

        if prices.max() != prices.min():

            normalized = (
                prices - prices.min()
            ) / (
                prices.max() - prices.min()
            )

        else:

            normalized = np.zeros(
                len(prices)
            )

        self.df["Normalized Price"] = (
            normalized
        )

    def create_computed_columns(self):

        self.df["Final Price"] = (
            self.df["Price"] *
            (
                1 -
                self.df["Discount"] / 100
            )
        )

        self.df[
            "Total Estimated Revenue"
        ] = (
            self.df["Final Price"] *
            self.df["Number of Reviews"]
        )

        self.df["Average Score"] = (
            self.df["Rating"] +
            self.df["Normalized Price"]
        ) / 2

    def find_hot_picks(self):

        average_reviews = (
            self.df[
                "Number of Reviews"
            ].mean()
        )

        self.hot_picks = self.df[
            self.df[
                "Rating Category"
            ].isin(
                ["Good", "Excellent"]
            )
            &
            (
                self.df[
                    "Number of Reviews"
                ]
                > average_reviews
            )
        ]

    def category_summary(self):

        return self.df.groupby(
            "Category"
        ).agg(
            total_products=(
                "Product ID",
                "count"
            ),
            average_price=(
                "Price",
                "mean"
            ),
            median_rating=(
                "Rating",
                "median"
            ),
            estimated_revenue=(
                "Total Estimated Revenue",
                "sum"
            )
        )

    def calculate_statistics(self):

        prices = self.df[
            "Price"
        ].tolist()

        return {
            "mean": statistics.mean(
                prices
            ),
            "median": statistics.median(
                prices
            ),
            "maximum": max(prices),
            "minimum": min(prices),
            "rounded_mean": math.ceil(
                statistics.mean(prices)
            )
        }

    def save_data(self):

        self.df.to_csv(
            "data/clean_products.csv",
            index=False
        )

        print(
            "Clean data saved."
        )


if __name__ == "__main__":

    processor = DataProcessor()

    processor.load_data()

    processor.clean_data()

    processor.create_categories()

    processor.create_list_comprehension()

    processor.create_tuples()

    processor.create_dictionaries()

    processor.create_numpy_features()

    processor.create_computed_columns()

    processor.find_hot_picks()

    print(
        processor.category_summary()
    )

    print(
        processor.calculate_statistics()
    )

    processor.save_data()


# In[ ]:




