# Airline Route Revenue Analysis

Multi-decade analysis of U.S. airline route revenue performance using Python and Tableau. This project evaluates domestic airline routes from 2010–2023, with a focus on estimated revenue, passenger demand, fare behavior, route ranking, revenue concentration, and seasonal trends.

> Note: This project analyzes estimated route revenue, not true profitability. Profitability would require cost data such as fuel, labor, aircraft utilization, airport fees, and operating expenses.

---

## Business Objective

Airlines operate across thousands of routes, but not all routes contribute equally to revenue. The goal of this analysis is to identify which routes generate the most estimated revenue, which routes underperform, and what factors appear to drive route performance.

This project answers the following business questions:

- Which routes generate the highest and lowest estimated revenue?
- How concentrated is revenue across top-performing routes?
- Do high-revenue routes perform better because of higher fares, higher passenger volume, longer distance, or a combination of factors?
- Are there seasonal trends in passenger demand or estimated revenue?
- How can airlines use route-level revenue segmentation to prioritize strategic decisions?

---

## Data Source + Grain

**Dataset Source:**  
U.S. Airline Flight Routes and Fares (1993–2024), available on Kaggle:  
https://www.kaggle.com/datasets/bhavikjikadara/us-airline-flight-routes-and-fares-1993-2024

**Original Dataset Grain:**  
The raw dataset contains U.S. domestic airline route and fare observations by year, quarter, origin city, destination city, fare, passengers, and distance.

**Analysis Grain:**  
For this project, the data was aggregated into two primary levels:

1. **Route-quarter level**  
   Used for seasonal and quarterly trend analysis.

2. **Route-year level**  
   Used for executive-level route ranking, revenue concentration, top/bottom route comparisons, and long-term trend analysis.

The final analysis focuses on complete years through 2023. The 2024 data was excluded because only partial-year data was available.

---

## Data Cleaning + Validation

The dataset was cleaned and validated in Python before being exported to Tableau for visualization.

Key cleaning and validation steps included:

- Standardized column names and formatting.
- Checked for missing values and incomplete records.
- Removed incomplete years from the final analysis.
- Validated that the dataset contained complete quarterly data for included years.
- Aggregated duplicate route-quarter observations into a consistent route-level structure.
- Confirmed that passenger, fare, distance, and revenue fields were usable for analysis.
- Excluded columns with high missingness from the core analysis.

Some carrier-level market share and lowest-fare pricing fields were excluded from the main analysis because they were missing in roughly 63%–66% of rows, which would weaken the reliability of the core route revenue analysis. :contentReference[oaicite:0]{index=0}

---

## Feature Engineering

To support route-level revenue analysis, several new fields were created:

- **Estimated Revenue:** calculated as `fare × passengers`
- **Weighted Average Fare:** calculated using passenger volume to avoid giving low-volume routes the same weight as high-volume routes
- **Clean Route Name:** created as `Origin City → Destination City` for Tableau readability
- **Revenue Deciles:** routes were grouped into top 10%, middle 80%, and bottom 10% based on estimated revenue
- **Route Rankings:** routes were ranked by estimated revenue and passenger demand

---

- ## Exploratory Analysis

The exploratory analysis focused on understanding how passenger demand, fare, distance, and estimated revenue interact across routes.

Key areas explored:

- Estimated revenue distribution
- Passenger volume differences across revenue groups
- Fare and distance patterns by route segment
- Seasonal trends by quarter
- Long-tail revenue concentration
- Differences between high-performing and low-performing routes

---

  ## Revenue Concentration

Revenue was highly concentrated among a small number of top-performing routes.

In 2023:

- The top 20 routes generated approximately $156.1M, or about 21.0% of total route revenue.
- The bottom 20 routes generated approximately $0.87M combined**, or about 0.12% of total route revenue.

This shows a long-tail revenue pattern where a small number of routes drive a large share of total revenue.

---

## Route Ranking: Top and Bottom Deciles

Routes were grouped into revenue deciles to compare high-performing, middle-performing, and low-performing routes.

Median passenger volume by group:

- **Top 10% routes:** 17,515 passengers
- **Middle 80% routes:** 2,599 passengers
- **Bottom 10% routes:** 238
- Top 10% routes carry ~74x more passengers than bottom 10% routes
- Top 10% of Routes Consistently Capture ~45% of Total Revenue

The top routes generated more revenue mainly because they carried far more passengers, not because fares or distance were dramatically different.

---

Key Findings
1. Passenger demand is the strongest driver of estimated route revenue

Top-performing routes generated significantly more revenue because they had much higher passenger volume. Fare and distance did not explain the gap as strongly as demand.

2. Revenue is highly concentrated

A small number of top routes produced a large share of total estimated revenue, while many low-performing routes contributed very little. This confirms a long-tail revenue pattern.

3. Low-performing routes are often demand-constrained

Bottom-tier routes had very low passenger volume, which limited their revenue potential even when fares were not dramatically lower.

4. Distance alone does not determine route performance

Longer routes do not automatically generate higher revenue. Passenger demand appears to matter more than route distance.

5. Decile segmentation makes route performance easier to explain

Grouping routes into top 10%, middle 80%, and bottom 10% made the analysis easier to communicate to a non-technical audience.

---

Recommendations
1. Protect and prioritize top-performing routes

High-revenue routes should receive priority for schedule stability, capacity planning, and customer experience improvements because they generate a large share of total revenue.

2. Review low-revenue routes for strategic fit

Routes in the bottom revenue tier should be reviewed to determine whether they serve a strategic purpose, such as market presence, network connectivity, or seasonal demand.

3. Use passenger demand as the primary route performance signal

Passenger volume should be a key metric when evaluating route health because it appears to be the clearest driver of estimated revenue.

4. Monitor route performance by segment, not just individually

Decile-based segmentation helps airlines identify broader patterns across route groups rather than reacting only to individual route performance.

5. Investigate low-demand routes before making cuts

Low-revenue routes should not automatically be removed. Airlines should evaluate seasonality, regional importance, connection value, and competitive positioning before making route decisions.

---

Limitations + Next Steps:

Limitations:
-This analysis uses estimated revenue, not profit.
-Operating costs were not included.
-Cost drivers such as fuel, aircraft type, labor, airport fees, and load factor were not available.
-Carrier-level competitive fields had substantial missing data and were excluded from the core analysis.
-The dataset does not fully explain why passengers choose specific routes.
-2024 was excluded because only partial-year data was available.
-Revenue estimates are based on fare and passenger volume, not full airline financial reporting.

---

Next Steps

Future analysis could improve the project by adding:

-Operating cost estimates by route
-Load factor or seat capacity data
-Airline carrier-level comparisons
-Airport-level market analysis
-Forecasting for future passenger demand or estimated revenue
-Competitive pricing analysis using complete carrier/fare fields
-Route profitability modeling if cost data becomes available

---

Tools Used:
-Python: data cleaning, validation, aggregation, feature engineering
-Pandas: data manipulation and route-level calculations
-NumPy: numerical calculations
-Tableau: dashboard creation, route segmentation, executive presentation visuals
-Jupyter Notebook: analysis documentation and workflow
-GitHub: project documentation and version control
---
Project Deliverables:

-Cleaned and aggregated route-level dataset
-Python data cleaning and analysis notebook
-Tableau dashboard/story presentation
-Route revenue segmentation analysis
-Executive summary of key findings and recommendations
-Tableau Dashboard

[[Add Tableau Public link here]](https://public.tableau.com/app/profile/emily.jackson7443/viz/Capstone2Final_17777646275400/Story1)
