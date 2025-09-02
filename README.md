# Superstore Sales Analysis Dashboard
An interactive Streamlit dashboard analyzing sales, profit, shipping modes, sub-categories, and regions.
Run the Dashboard Live: https://data-analysis-for-superstore-dataset-dfry8kegut6slojoewgrbw.streamlit.app/

## Project Background
This project analyzes the Superstore dataset.
Superstore dataset is a publicly available datset of sales for a fiction US superstore. The dataset simulates a real retail superstore, offering realistic business scenarios for analysis.It is commonly used for data analysis and visualization practice.

The data consists of sales, profits, ship modes, regions, discounts etc. from year 2014 to 2017. 
This project analyzes these features to provide insights and recommendations for the following areas:
1. Sales/ Profit yearly trends: Analyzing monthly average sales and profit line charts for each year to observed how each month performs on an average and identify overall seasonality trends.
2. Shipping Mode vs Sales and Profit: Analyzing how profit and sales are affected by different ship modes, to understand which modes drive the highest performance and profitability.
4. Sub-Category vs Sales or Profits: Analyzing sales and profit across different product sub-categories to identify top performing and under performing categories.
5. Region vs Sales or profits: Analyzing regional sales and profit to compare performance across different regions (central, east, west, south)

##  Data Structure 
Source: Kaggle -Sample Superstore Dataset (https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
Features: Order ID, Customer Name, Segment, Category, Sub-Category, Sales, Quantity, Discount, Profit, Region, State, Ship Mode, etc.

<img width="450" height="300" alt="image" src="https://github.com/user-attachments/assets/44657c74-827d-461d-b92b-d9bc6ad781a7" />

## Executive Summary
### Overview of findings
### Sales Trends
Insight: 
1. Sales usually go up in March, September, and October, while they slow down in February and April. 
2. But profits don’t always rise when sales do, which means things like discounts or the type of products sold might be affecting the bottom line.

Recommendation: 
1. Plan your big campaigns and promotions around March, September, and October when customers are already buying more.
2. For slower months like February and April, try offering special discounts, bundles, or loyalty deals to keep sales steady.
   
<img width="1688" height="788" alt="image" src="https://github.com/user-attachments/assets/6d1945d7-13e1-4fa9-ae5f-175f13b17045" />

### Sales and Profit by Shipping Mode
Insights:
1. Standard Class contributes the highest sales and profit, showing it is the most popular shipping option.
2. Same Day has the lowest sales and profit, it suggests that demand is limited for fast delivery.
3. Customers seem to prefer lower-cost shipping options over fast delivery.
4. The modes with more sales bring more profit.

Recommendations:
1. Make Standard Class reliable as it drives more sales.
2. Second Class can be promoted as a good middle option with some offers.
3. First Class, not much should be spent on this as it adds less value.
4. Same Daymode is not used by many but is important for customers who need urgent delivery.
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/fab6c479-5833-4beb-863c-96aefe0404f0" />
<img width="900" height="266" alt="image" src="https://github.com/user-attachments/assets/18d122ac-0541-483b-83e7-6b76f41ff368" />

### Sales and Profit by Sub-Category
Insights:
1. Profitability differs a lot by sub-category.
2. High profit drivers: Copiers, Phones, Accessories.
3. Moderate contributors: Chairs, Furnishings, Storage.
4. Low profit categories: Fasteners, Machines, Labels, Art, Envelopes.
5. Negative profit categories: Tables, Bookcases,Supplies.
6. Negative profit categories generate losses due to some products have very high discounts (upto 70%) and also have negative profit margins, meaning every sale in these 
   categories results in a loss.
   
Recommendations:
1. Focus more on High profit category since they make the most profit.
2. Try to grow Moderate profit category with better promotions and bundles.
3. For Low profit categories don’t spend too much on them.
4. For negative profit categories control big discounts, check pricing, and remove products that always cause losses
<img width="1124" height="526" alt="image" src="https://github.com/user-attachments/assets/d872e808-04d5-4339-b716-3a0db4a7b88a" />
<img width="702" height="581" alt="image" src="https://github.com/user-attachments/assets/e2f635b6-2ee0-4ac4-8ef9-63fbe2f75b0f" />

### Sales and Profit by Region
Insights:
1. West has the largest share in both sales and profit- the most important region.
2. East is the second strongest, contributing well in sales as well as profit.
3. Central has a fair share of sales but a much smaller profit share.
4. South contributes the least in sales but does slightly better in profit than Central.

Recommendations:
1. For East and West keep investing, they are the main growth drivers.
2. For Central review pricing, discounts, or costs to improve profitability.
3. For South explore growth opportunities (marketing, product expansion), since it converts sales into profit better than Central.
<img width="1090" height="483" alt="image" src="https://github.com/user-attachments/assets/ba210cf1-eb1a-4887-a554-15e53d57abbb" />
<img width="1248" height="362" alt="image" src="https://github.com/user-attachments/assets/cde80d24-529c-4793-ae45-7f51c8e99808" />

## Author
Dia Singh- https://www.linkedin.com/in/dia-singh-31486a220/

