import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data.csv")

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
region_sales.plot(kind="bar", title="Sales by Region")
plt.show()
