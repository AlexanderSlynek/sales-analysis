Sales Analysis

Sales data analysis and visualization project using Python, Pandas and Matplotlib.

Repository:
https://github.com/AlexanderSlynek/sales-analysis

⸻

Project Overview

This project analyzes sales data stored in a CSV file and calculates key business metrics such as:

* Total revenue
* Revenue by product
* Revenue by category
* Revenue by date
* Sales volume
* Average selling price

The project was created as a practical exercise in data analysis with Python and Pandas.

⸻

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

Files

* data/sales.csv — source sales dataset
* sales_analysis.py — main Python script containing the analysis and visualizations
* requirements.txt — project dependencies
* .gitignore — files excluded from Git
* README.md — project documentation

⸻

Technologies

* Python
* Pandas
* Matplotlib

⸻

Data Processing

The dataset contains information about:

* Date
* Product
* Category
* Quantity
* Price

Processing Steps

1. Load the CSV file using Pandas.
2. Convert dates to the datetime format.
3. Convert Quantity and Price to numeric values.
4. Remove the $ symbol from prices.
5. Calculate revenue for every sale:

Revenue = Quantity × Price

6. Group the data by product, category, and date.

⸻

Analysis

The project calculates:

* Total revenue
* Revenue by product
* Revenue by category
* Revenue by date
* Quantity sold for each product
* Average selling price for each product
* Product with the highest revenue
* Best-selling product
* Day with the highest revenue
* Product with the highest average selling price

⸻

Visualizations

The project generates the following charts:

* Revenue by product
* Revenue by category
* Revenue over time
* Number of products sold
* Average selling price by product

⸻

How to Run

1. Clone the repository

git clone https://github.com/AlexanderSlynek/sales-analysis.git

2. Navigate to the project directory

cd sales-analysis

3. Install dependencies

pip install -r requirements.txt

4. Run the analysis

python sales_analysis.py

⸻

What I Learned

This project helped me practice:

* Reading CSV files with Pandas
* Data cleaning and type conversion
* Working with dates
* Creating calculated columns
* Using groupby()
* Aggregating data with sum()
* Using max() and idxmax()
* Working with Pandas Series
* Data visualization
* Writing reusable Python functions
* Organizing a Python project for GitHub

⸻

Future Improvements

Possible improvements for future versions include:

* Adding more statistical analysis
* Improving chart formatting
* Adding additional business metrics
* Creating an interactive dashboard
* Using the processed data for a machine learning project

⸻

Author

Alexander Slynek

This project is part of my learning path toward Machine Learning and Financial Machine Learning.