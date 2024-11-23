import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# create a function to load the dataset. we gave the tab space below so it will be inside the same function
def load_data():
    df = pd.read_csv("supermarket_sales new.csv")
    df.loc[:,"Revenue"] = (df['Unit price'] * df['Quantity']) - df['Tax 5%']

    return df
    
# load the data
data = load_data()

# create a title for the app
st.title("SuperMarket Sales Analysis")

# add a filter. the sign {} means to open a dictionary.
filters = {
    "Gender": data["Gender"].unique(),
    "Branch": data["Branch"].unique(),
    "City": data["City"].unique(),
    "Customer type": data["Customer type"].unique(),
    "Product line": data["Product line"].unique(),
}
# store user selection
selected_filters = {}

# generate multi-select widgets dynamically in the side bar
for key, options in filters.items():
    selected_filters[key]=st.sidebar.multiselect(key,options)
# add a dynamic filter
filtered_data = data # start with the full data (if returns if true or false)
for key, selected_values in selected_filters.items():
    if selected_values:
        filtered_data = filtered_data[filtered_data[key].isin(selected_values)]

# after writing from line 19- 37, click 'ctrl s' and go to your app (browser) where you have the table, click refresh arrow on the top left habd side. then you will see the side bar with the key options. 

# to tryu out the fiter,anywhere you have 'data', you can write 'filtered_data' to it , to help u filter the data just as in line 47 -50 and line 98.
# where you have'data["Revenue"].sum()' in line 50, write 'filtered_data["Revenue"].sum()' and go to your table on your browser to refresh so the changes can be made

# display in the browser
st.dataframe(filtered_data)


# calculate total revenue, total qty, avg unitprice, avg tax
no_of_items = len(data)
total_revenue = data["Revenue"].sum()
total_qty = data["Quantity"].sum()
avg_price = data["Unit price"].mean()
avg_tax = data["Tax 5%"].mean()

# streamlit column component
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("No of Items", no_of_items)

with col2:
     st.metric("Total Revenue", total_revenue)

with col3:
    st.metric("Total Qty", total_qty)

with col4:
    st.metric("Avg Unit price", avg_price)

with col5:
     st.metric("Avg Tax", avg_tax)

# to streamline colunn component to appear in your browers under the barchat:
# go to your cmd, stop the previous one from running by clicking ctrl C. then type'streamlit run app.py'
# click enter  and go to your browser and click the options beside the table and click rerun.

# always do ctrl s to save. 

# line 17 showing st.dataframe(data) means after u have created a title on the table that will show on your browser,then st.dataframe is the formula 
# for showing the data. hence the data is shown.

# to show the new table with the heading "SuperMarket Sales Analysis" in your browser, do the below steps.
# cmd - command directory. go to your search button in your laptop and type command prompt to see it.
# type"cd app" in the last cursor in your command pronpt , click enter.
# then type "streamlit run app.py" and run it by clicking enter, the table wil show in your browser.

# to start another to run or downlaod,
# press ctrl c in your CMD to stop the file from running.
# it will take u to a new line that has '(env) C:\Users\pc\Documents\PYTHON CLASS FILES\DATAAPPS\app>'
# your cursur will be showing on that line above , then type 'pip install plotly' and click enter.
# after some mins, u will see suyccessfully installed plotly


# find the product line with the highest revenue
# use a bar chart

con = st.container()

with con:
    # plotly chart
    bar1 = px.bar(data,x="Product line", y="Revenue")
    st.plotly_chart(bar1)


# to get a bar chart on your browser in the same page showing the ("SuperMarket Sales Analysis") table, fo this below:
# type "streanlite run app.py" on the last line where your cursor is, then click enter.
# go to your broswer that has the table, check the 3 dots(option sign) on your right top beside the table,click rerun.
# the bar chart will appear.

# NB:anytime you correct an error (like in caps or small leter, or input a word), in this current app page, always  click "ctrl s'to save

# do ctrl c to stop running then type 'pip list' in your cmd new line,  to show you list of all the libraries that were installed
# to see streamlit- type streamlit on google, click the ist line, click 'doc' on your right hand, click 'streamlit documenetation' then 'API reference' to see alot of details and formula.


