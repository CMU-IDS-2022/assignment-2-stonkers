pip install yfinance
import pandas as pd
import yfinance as yf

import altair as alt
from pandas_datareader import data
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
# For reading stock data from yahoo
from datetime import datetime



st.title("Did the crypto volatility affect stock prices?")
st.caption("1. Here, we can select Bitcoin and any other stock for comparison. Select two, or multiple stocks for comparison")



stock_list = ('BTC-USD','ETH-USD','TSLA','AAPL', 'GOOG', 'MSFT', 'AMZN')

dropdown = st.multiselect('Select stocks for comparison', stock_list)

start = st.date_input('Start',value=pd.to_datetime('2021-01-01'))
end = st.date_input('End',value=pd.to_datetime('today'))

def stock_returns(df):
    rel=df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    df = stock_returns(yf.download(dropdown,start,end)['Adj Close'])
    st.line_chart(df)





df = stock_returns(yf.download(stock_list,start,end)['Adj Close'])


#Interaction = stock_returns(yf.download(stock_list,datetime(end.year - 1, end.month, end.day),end)['Adj Close'])

df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Date'})

df= df.melt(id_vars="Date")
df=df.rename(columns={"Date": "date", "variable": "company", "value": "return"})

portfolio=df

interval = alt.selection_interval(encodings=['x'])

scatter = alt.Chart(portfolio).mark_line().encode(
    x='date',
    y='return',
    color='company',
).properties(
    width=550,
    selection=interval
)


bar = alt.Chart(portfolio).mark_bar().encode(
    x='average(return)',
    y='company',
    color='company',
  ).properties(
      width=550,  
).transform_filter(
    interval
)

return_comparison_viz = scatter & bar


st.title("Did the crypto volatility affect stock returns?")
st.caption("Both the visualization represent stock returns over the last year. Click on the graph and select a time-period you want to explore. Slide your selection across the graph, to view the change in returns for each stock at the bottom ")

st.write(return_comparison_viz)

st.markdown("This project was created by Urvish Thakkar and Princy Sasapara for the Interactive Data Science(https://dig.cmu.edu/ids2022) course at Carnegie Mellon University (https://www.cmu.edu).")
