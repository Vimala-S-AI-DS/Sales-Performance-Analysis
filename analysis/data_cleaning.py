import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

print(df.head())
print(df.isnull().sum())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

print("Data cleaned successfully")
