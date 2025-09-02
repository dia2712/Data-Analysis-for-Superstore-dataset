import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Superstore sales analysis report")

df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
df['Order Date']=pd.to_datetime(df['Order Date'])
df['month']=df['Order Date'].dt.month
df['year']=df['Order Date'].dt.year

tab1,tab2,tab3,tab4=st.tabs(['overall sales health','Ship Mode vs Sales and Profit','Profitability by Sub-Category','Regional View'])

st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] div[data-testid="stMetric"] {
            font-size: 1.0em; /* Adjust as needed */
        }
        section[data-testid="stSidebar"] div[data-testid="stMetricLabel"] {
            font-size: 1.0em; /* Adjust as needed */
        }
        section[data-testid="stSidebar"] div[data-testid="stMetricValue"] {
            font-size: 1.0em; /* Adjust as needed */
        }
        section[data-testid="stSidebar"] div[data-testid="stMetricDelta"] {
            font-size: 1.0em; /* Adjust as needed */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
st.sidebar.metric(label="Total Sales ", value=f"${df['Sales'].sum():,.0f}")
st.sidebar.metric(label="Total Profit ", value=f"${df['Profit'].sum():,.0f}")
st.sidebar.metric(label="Avg Order value ", value=f"${df['Sales'].mean():,.0f}")

BOLD = '\033[1m'
END = '\033[0m'

with tab1:

    # create 2x2 subplot
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("2014", "2015", "2016", "2017")
    )

    years = [2014, 2015, 2016, 2017]
    positions = [(1,1), (1,2), (2,1), (2,2)]

    for year, pos in zip(years, positions):
        yearly_data = df[df['Order Date'].dt.year == year]
        sales_profit = yearly_data.groupby(yearly_data['Order Date'].dt.month)[['Sales','Profit']].sum().reset_index()
        sales_profit.rename(columns={'Order Date':'month'}, inplace=True)
        
        # add sales line
        fig.add_trace(
            go.Scatter(x=sales_profit['month'], y=sales_profit['Sales'], mode="lines+markers", name=f"Sales {year}"),
            row=pos[0], col=pos[1]
        )
        
        # add profit line
        fig.add_trace(
            go.Scatter(x=sales_profit['month'], y=sales_profit['Profit'], mode="lines+markers", name=f"Profit {year}"),
            row=pos[0], col=pos[1]
        )

    fig.update_layout(
        height=800, width=1000,
        title_text="Monthly Average Sales & Average Profit Trends by Year",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write('''The graph displays the average sales and average profit for each month, broken down by year.

**Insight:** Sales usually go up in March, September, and October,
while they slow down in February and April. But profits don’t always rise when sales do,
which means things like discounts or the type of products sold might be affecting the bottom line.

**Recommendation:** Plan your big campaigns and promotions around March, September, and October when customers are already buying more. For slower months like February and April, try offering special discounts, bundles, or loyalty deals to keep sales steady.''')



with tab2:
    ship_data = df.groupby("Ship Mode")[["Sales","Profit"]].sum().reset_index()
    # Setup for side-by-side bars
    x = np.arange(len(ship_data["Ship Mode"]))  # positions
    width = 0.35
    fig = px.bar(
        ship_data,x="Ship Mode",y=["Sales","Profit"],barmode="group",title="Sales vs Profit by Shipping Mode")
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
<div style="font-size:14px;">
<ul>
<b>Insights:</b>
<li>Standard Class contributes the highest sales and profit, showing it is the most popular shipping option.</li>
<li>Same Day has the lowest sales and profit, it suggests that demand is limited for fast delivery.</li>
<li>Customers seem to prefer lower-cost shipping options over fast delivery.</li>
<li>The modes with more sales bring more profit.</li>
<b>Recommendations:</b>
<li>Make <b>Standard Class</b> reliable as it drives more sales.</li>
<li><b>Second Class</b> can be promoted as a good middle option with some offers.</li>
<li><b>First Class</b>, not much should be spent on this as it adds less value.</li>
<li><b>Same Day</b>mode is not used by many but is important for customers who need urgent delivery.</li>
""",unsafe_allow_html=True)

    st.dataframe(ship_data)


with tab3:
    SubSum=df.groupby(['Sub-Category'])['Profit'].sum().reset_index()
    SubSum['color'] = SubSum['Profit'].apply(lambda x: '#FF0000' if x<0 else '#008000')
    st.bar_chart(SubSum,x='Sub-Category',y='Profit',color='color')

    st.markdown("""
    <div style="font-size:14px;">
    <ul>
    <b>Insights:</b>This graph represents profit for each sub-category.
    <li>Profitability differs a lot by sub-category.</li>
    <li><b>High profit drivers:</b> Copiers, Phones, Accessories.</li>
    <li><b>Moderate contributors:</b> Chairs, Furnishings, Storage.</li>
    <li><b>Low profit categories:</b> Fasteners, Machines, Labels, Art, Envelopes.</li>
    <li><b>Negative profit categories:</b> Tables, Bookcases,Supplies.
    <li>Negative profit categories generate losses due to some products have very high discounts (upto 70%) and also have negative profit margins,
     meaning every sale in these categories results in a loss.</li> 
    <b>Recommendations:</b>
    <li>Focus more on High profit category since they make the most profit.</li>
    <li>Try to grow Moderate profit category with better promotions and bundles.</li>
    <li>For Low profit categories don’t spend too much on them.</li>
    <li>For negative profit categories control big discounts, check pricing, and remove products that always cause losses</li>
    """,unsafe_allow_html=True)
    st.dataframe(SubSum)
    

with tab4:
    regSales=df.groupby('Region')['Sales'].sum().reset_index()
    regProfit=df.groupby('Region')['Profit'].sum().reset_index()
    regSales['Profit']=regProfit['Profit']
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    # Sales Donut
    axes[0].pie(regSales['Sales'], labels=regSales['Region'], autopct='%1.1f%%',
                startangle=90, wedgeprops=dict(width=0.4))
    axes[0].set_title("Sales Share")

    # Profit Donut
    axes[1].pie(regSales['Profit'], labels=regSales['Region'], autopct='%1.1f%%',
                startangle=90, wedgeprops=dict(width=0.4))
    axes[1].set_title("Profit Share")
    st.pyplot(fig)
    
    st.markdown("""
    <div style="font-size:14px;">
    <ul>
    <b>Insights:</b>This graph represents profit for each sub-category.
    <li><b>West</b> has the largest share in both sales and profit- the most important region.</li>
    <li><b>East</b> is the second strongest, contributing well in sales as well as profit.</li>
    <li><b>Central</b> has a fair share of sales but a much smaller profit share.</li>
    <li><b>South</b> contributes the least in sales but does slightly better in profit than Central.</li>
    <b>Recommendations:</b>
    <li>For <b> East and West</b> keep investing, they are the main growth drivers.</li>
    <li>For <b>Central</b> review pricing, discounts, or costs to improve profitability.</li>
    <li>For <b>South</b> explore growth opportunities (marketing, product expansion), since it converts sales into profit better than Central.</li>
    """,unsafe_allow_html=True)

    st.dataframe(regSales)

st.sidebar.dataframe(df)

