import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/sales.csv")
df["Date"] = pd.to_datetime(df["Date"], format = "%d.%m.%Y")
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Price"] = df["Price"].str.replace("$", "", regex = False).str.strip()
df["Price"] = pd.to_numeric(df["Price"])
df["Revenue"] = df["Quantity"] * df["Price"]
total_revenue = df["Revenue"].sum()
product_revenue = df.groupby("Product")["Revenue"].sum()
category_revenue = df.groupby("Category")["Revenue"].sum()
date_revenue = df.groupby("Date")["Revenue"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()
average_price = product_revenue / product_quantity

def revenue_by_product_chart():
    product_revenue.plot(kind = "bar")
    plt.title("Graphic of total revenue of products in bar chart")
    plt.xlabel("Product")
    plt.ylabel("Revenue ($)")
    plt.show()

def revenue_by_category_chart():
    category_revenue.plot(kind = "bar")
    plt.title("Graphic of total revenue of categories in bar chart")
    plt.xlabel("Category")
    plt.ylabel("Revenue ($)")
    plt.show()

def revenue_by_date_chart():
    date_revenue.plot()
    plt.title("Graphic of total revenue by date")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.show()

def number_of_sold_products_chart():
    product_quantity.plot(kind = "bar")
    plt.title("Graphic of number of sold products")
    plt.xlabel("Product")
    plt.ylabel("Number of sold ones")
    plt.show()

def average_price_chart():
    average_price.plot(kind = "bar")
    plt.title(" Average price of every sold product")
    plt.xlabel("Product")
    plt.ylabel("Price ($)")
    plt.show()

print(category_revenue)
print("The most profitable product:", product_revenue.idxmax())
print("The amount of revenue:", product_revenue.max())
print("The most profitable day:", date_revenue.idxmax())
print("Revenue of that day:", date_revenue.max(), "$" )
print("Best-selling product:", product_quantity.idxmax())
print("Number of that product that were sold:", product_quantity.max())
print("Total revenue:", total_revenue, "$")
print("Product with highest average price:", average_price.idxmax())
print("Average price:", average_price.max())
print(df.head())
df.info()
revenue_by_product_chart()
revenue_by_category_chart()
revenue_by_date_chart()
number_of_sold_products_chart()
average_price_chart()
