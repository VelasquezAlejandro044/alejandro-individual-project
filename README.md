# Wlamart weekly sales for 45 stores

Individual Projects
-----------------------

## Purpose:
This project aims to analyze the sales of 45 Walmart stores between 2010-01-10' to '2012-12-10'

## Goal

Use 143 weeks of data to find a time series model that will allow us to predict weekly sales.
Deliverables

# Main question 

What Time Series Analysis tool is better fit to forecast sales?

# Plan

- Use Trello to plan workload
https://trello.com/b/DBgM4r0v/individual-project

- Acquire and prepare Walmart sales found on kaggle.com. 
Analysis based on Time Series modeling and ran through the data pipeline.

- Use visuals to understand the data and find the best performing Model.

- Github Repo w/ Final Jupyter Notebook and README

- Project summary and writeup for your resume or other professional portfolio pieces

----------------------------

### Data Dictionary
<table>
<thead><tr>
<th>Variable</th>
<th>Meaning</th>
</tr>
</thead>                                                            
<tbody>
<tr>
<td>Weekly Sales</td>
<td>Amount US dollars sold per every week</td>
<tr>
<td>Seasonality</td>
<td>A repeated cycle in the data. Occurs at a fixed frequency.</td>
</tr>
</tbody>
</table>

-------------------------------
## Key findings and Recomendations

- Running a simple average is a handy tool that could make forecasting at Walmart more simple for leadership

- Christmas and Black Friday are the best seasons for the stores.

- January and September are the months with fewer sales of the year

- We would want to get a data set that has at least three years worth of data so that we perform other time series analysis  algorithms such as Holts Linear Trend and Previous cycle 

- If I had more time, I would analyze stores individually to see if some of them experience a different type of seasonality 

- Run regression models that will allow us to understand how different stores react to gas price changes, temperature changes, and unemployment changes.

## To recreate:

### Modules
- wrangle.py
Functions to acquire, prepare, and split data
- viz.py
Functions to create visualizations
- model.py
It helps with the creation and visualization of models 
-  report_final_walmart_tsa_weekly_sales.ipynb
Contains functions that would allow graphing, calculation, and comparison of RMSE 

### Data set to recreate 
https://github.com/VelasquezAlejandro044/alejandro-individual-project/blob/main/Walmart.csv

Walmart.csv

