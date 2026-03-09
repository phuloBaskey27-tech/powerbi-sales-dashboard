import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("sales_data.csv")

# total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# total profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# sales by region
sales_region = df.groupby("Region")["Sales"].sum()
print(sales_region)

# plot chart
sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.show()
