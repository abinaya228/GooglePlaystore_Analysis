# Google Play Store App Analysis

## Overview
This project analyzes the Google Play Store dataset to extract insights about app categories, ratings, installs, and other key metrics. The analysis is performed using **Python**, leveraging libraries such as **pandas**, **numpy**, **matplotlib**, and **seaborn**.

The goal of this project is to understand patterns in app popularity, pricing, and category performance, similar to visualizations created in Tableau, but implemented programmatically in Python.

---

## Dataset
- **File:** `task1-Sheet1.csv`  
- **Source:** Public Google Play Store dataset (can be downloaded from Kaggle or other open datasets)  
- **Rows:** 9,659 apps  
- **Columns:** 17 attributes including App Name, Category, Rating, Reviews, Size, Installs, Type, Price, and more.  

**Note:** The dataset was cleaned as part of this project to handle missing values and ensure proper numeric conversions for analysis.
---

## Features of the Analysis
The script `googleplay.py` performs the following:

1. **Data Cleaning & Preparation**
   - Converts columns like `Installs`, `Size`, and `Price` into numeric formats.
   - Handles missing values for ratings and size columns.

2. **Visualization 1: App Count and Average Rating by Category**
   - Bar chart showing the number of apps per category.
   - Color-coded by average rating.

3. **Visualization 2: Free vs Paid Apps**
   - Pie chart showing the distribution of free vs paid apps.
   - Bar chart comparing average ratings for free and paid apps.

4. **Visualization 3: Size vs Rating Relationship**
   - Scatter plot of app size vs rating.
   - Trendline added to identify correlation.
   - Color-coded by number of installs.

5. **Visualization 4: Category Performance Quadrant Analysis**
   - Scatter plot comparing average installs and ratings per category.
   - Quadrant labels (Stars, Mass Market, Niche, Avoid) based on averages.
   - Bubble size represents the number of apps in that category.

6. **Optional Advanced Analysis**
   - Correlation heatmap between key numeric features (Rating, Reviews, Installs, Size, Price).

---

## How to Run
1. Ensure you have Python 3.x installed.
2. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn
