# NPower-Group-2-mini-Project
Just a mini Group 2 Project /Exercise for Data Cleaning and Data Wrangling using  E-Commerce_Sales_Analysis

## E-Commerce Sales Data Analysis
Project Overview

This project analyzes an online retail e-commerce dataset to understand sales performance, customer behaviour, product demand, and purchasing patterns across different countries and time periods.

The main objective of this project was to clean and prepare the raw transaction data, perform exploratory data analysis, answer key business questions, and create insights that could support better business decisions.

This project was completed as part of the NPower Canada Junior Data Analyst program.

## Dataset
UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/352/online+retail,

Kaggle: https://www.kaggle.com/datasets/carrie1/ecommerce-data

The original dataset used for this project is the Online Retail dataset, which contains transaction records for an online retail business.

Due to GitHub file-size limits, the raw and cleaned CSV files are not included in this repository.

To run the project, download the original dataset separately, place it in the project folder, and make sure the file name matches the file name used in the cleaning notebook.

The cleaning notebook will process the original dataset and create the cleaned CSV file needed for the final analysis notebook.

## Project Files

The project contains the following main files:

<li>Final-Cleaning.ipynb-Cleans the original dataset and creates the cleaned CSV file.
<li>Final-Analysis.ipynb-Performs exploratory data analysis and creates visualizations using the cleaned dataset.
<li>E-commerce_Sales_Analysis_Report.pdf-Final written report.
<li>README.md


The large CSV data files are excluded from this repository because they exceed GitHub upload limits.

## Business Questions

The analysis focused on answering the following questions:

Which countries generated the highest total sales?
What were the monthly sales trends?
How did new and returning customers behave over time?
What purchasing patterns existed by day, hour, and time of day?
Which products were the best-selling overall?
Which products performed best by country?
Who were the top customers by total sales?
How did sales compare with returns and cancellations?

## Data Cleaning Process

The raw dataset contained duplicates, missing values, cancelled transactions, stock adjustments, and zero-price records. The following cleaning steps were performed:

Loaded the dataset using the appropriate encoding.
Checked the structure of the dataset using df.info(), df.describe(), and missing value counts.
Removed duplicate rows.
Converted the InvoiceDate column to datetime format.
Identified cancelled transactions using invoice numbers that started with "C".
Investigated negative quantities to separate returns/cancellations from stock or accounting adjustments.
Removed zero-price transactions because they did not represent actual sales.
Removed non-sales adjustment records.
Created a cleaned dataset for analysis.
Created new date and time columns from the invoice date.
Created a Total_Sales column using:
Total_Sales = Quantity * UnitPrice

## Feature Engineering

Additional columns were created to support deeper analysis:

Total_Sales
InvoiceYear
InvoiceMonth
InvoiceDayName
InvoiceHour
YearMonth
Invoice_Time_of_Day
CustomerID_Label

These new columns made it easier to analyze sales trends, customer behavior, and purchasing patterns.

## Exploratory Data Analysis

The analysis included:

Total sales by country
Monthly sales trends
Top countries by sales
New versus returning customer trends
Sales activity by day of the week
Sales activity by hour of the day
Sales activity by time of day
Top-selling products by quantity
Best-selling product by country
Top customers by total sales
Sales versus cancellations/returns

Visualizations were created using Python libraries such as Matplotlib, Pandas, and Plotly.

## Dashboard Concept

A dashboard was also designed to present the key findings in a more interactive way.

The dashboard concept includes:

KPI cards for total sales, number of invoices, number of customers, and total quantity sold.
Dropdown filters for country, month, and transaction type.
Charts showing:
Top countries by sales
Monthly sales trends
Best-selling products
Sales by time of day

The dashboard was planned using Plotly Dash.

## Tools and Technologies Used
Python
Pandas
NumPy
Matplotlib
Plotly
Dash
Jupyter Notebook
GitHub

Project Files

## The project contains the following main files:

Final-Cleaning.ipynb
Cleans the original dataset and creates the cleaned CSV file.
Final-Analysis.ipynb
Performs exploratory data analysis and creates visualizations.
Online_Retail_clean2.csv
Cleaned dataset used for analysis.
README.md
Project description and instructions.

## Key Insights

Some of the main insights from the analysis include:

A small number of countries contributed the majority of total sales.
Sales activity varied by month, showing clear monthly trends.
Returning customers played an important role in ongoing sales activity.
Purchasing activity was stronger during certain times of the day.
A small group of products accounted for a high quantity of items sold.
Returns and cancellations needed to be separated from regular sales to avoid misleading results.

## Conclusion

This project demonstrates the full data analysis workflow, including data cleaning, feature engineering, exploratory data analysis, and visualization.

Due to the time constraints of the project, the data cleaning process was focused on preparing the dataset well enough to answer the required business questions accurately. The cleaning process addressed the most important issues, including duplicates, missing values, cancelled transactions, returns, stock adjustments, and zero-price records.

The analysis shows the importance of carefully reviewing transaction data before drawing business conclusions. By separating valid sales from cancellations, returns, stock adjustments, and non-sales records, the final analysis provides a more accurate view of customer behaviour and sales performance.

An additional report, **E-Commerce Sales Analysis Report**, has been included as a PDF file in this repository. The report provides a written summary of the project, key business questions, analysis, visualizations, and conclusions.

This project also provides a strong foundation for building an interactive business dashboard using Plotly Dash or Power BI.

