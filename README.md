Sales Analysis

Sales data analysis and visualization project using Python, Pandas and Matplotlib.

Repository

GitHub Repository

Project Overview

This project analyzes sales data stored in a CSV file and calculates key business metrics such as total revenue, revenue by product and category, sales volume, and average selling price.

The project was created as a practical exercise in data analysis with Python and Pandas.

Project Structure

sales-analysis/

│

├── data/

│   └── sales.csv

│

├── sales_analysis.py

├── README.md

├── requirements.txt

└── .gitignore

Files and Directories

data/sales.csv — source sales dataset.
sales_analysis.py — main Python script containing the analysis and visualizations.
requirements.txt — Python dependencies required to run the project.
.gitignore — files and directories that should not be uploaded to GitHub.
README.md — project documentation.
Technologies

Python
Pandas
Matplotlib
Data Processing

The dataset contains information about:

Date
Product
Category
Quantity
Price
During the analysis:

The CSV file is loaded using Pandas.
Dates are converted to the datetime format.
Quantity and Price are converted to numeric values.
The $ symbol is removed from the Price column.
Revenue is calculated for every sale:
Revenue = Quantity × Price

The data is grouped by product, category and date.
Analysis

The project calculates:

Total revenue
Revenue by product
Revenue by category
Revenue by date
Quantity sold for each product
Average selling price for each product
Product with the highest revenue
Best-selling product
Day with the highest revenue
Product with the highest average selling price
Visualization

The project generates several charts:

Revenue by product
Revenue by category
Revenue over time
Number of products sold
Average selling price by product
How to Run

Clone the repository and navigate to the project directory.

Install the required dependencies:

pip install -r requirements.txt

Run the analysis:

python sales_analysis.py

What I Learned

This project helped me practice:

Reading CSV files with Pandas
Cleaning and converting data
Working with dates
Creating calculated columns
Using groupby()
Aggregating data with sum()
Finding maximum values with max() and idxmax()
Working with Pandas Series
Creating visualizations
Writing reusable Python functions
Organizing a Python project for GitHub
Future Improvements

Possible improvements for future versions include:

Adding more detailed statistical analysis
Improving chart formatting
Adding additional business metrics
Creating an interactive dashboard
Using the processed data for a machine learning project
Author

Alexander Slynek

This project is part of my learning path toward Machine Learning and Financial Machine Learning.
