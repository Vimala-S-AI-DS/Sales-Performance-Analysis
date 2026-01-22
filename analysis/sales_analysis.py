import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

# Total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

# Profit by product
product_profit = df.groupby("Product")["Profit"].sum()
print(product_profit)
