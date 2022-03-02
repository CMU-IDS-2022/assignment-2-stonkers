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


st.header("Part A: Exploring the volatility")
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
st.caption("2. Both the visualization represent stock returns over the last year. Click on the graph and select a time-period you want to explore. Slide your selection across the graph, to view the change in returns for each stock at the bottom ")

st.write(return_comparison_viz)

st.header("Part B: Dwelling into the Percentages")
st.title("Does History repeat itself!")
st.subheader("Enter the Stock Code:")

st.caption("Please enter the stock code (ticker code) which you want to analyse and see visualizations for. We are using Yahoo Finance API to fetch the real-time data, and here we can render visulizations for all stock.")

stock_ticker = st.text_input("Please enter the ticker code for stock whose analysis you would like to Visualize", 'AAPL')

#stock_ticker = 'SNAP'
# start = pd.to_datetime(['2007-01-01']).astype(int)[0]//10**9 # convert to unix timestamp.
start = pd.to_datetime(['today']) - pd.DateOffset(years=5)
start = start.astype(int)[0]//10**9 
# start = pd.to_datetime(['today']-5).astype(int)[0]//10**9 # convert to unix timestamp.
end = pd.to_datetime(['today']).astype(int)[0]//10**9
# end = pd.to_datetime(['2020-12-31']).astype(int)[0]//10**9 # convert to unix timestamp.
url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock_ticker + '?period1=' + str(start) + '&period2=' + str(end) + '&interval=1d&events=history'
df = pd.read_csv(url)

def daily_percent_change(df):
  df.loc[0, '% Change'] = 0
  for i in range(1, len(df)):
    df.loc[i, '% Change'] = ((df.loc[i,'Adj Close'] - df.loc[i-1,'Adj Close']) / df.loc[i-1,'Adj Close']) * 100
  return df

df = daily_percent_change(df)

df_top_10_positive = df.sort_values('% Change').tail(10)

df_top_10_negative = df.sort_values('% Change').head(10)

top_positive = alt.Chart(df_top_10_positive).mark_bar(color='green',tooltip=True).encode(
    x = 'Date',
    y = '% Change'
).properties(
    title='Top 10 Positive percentage changes for the Stock'
)

top_negative = alt.Chart(df_top_10_negative).mark_bar(color='red', tooltip=True).encode(
    x = 'Date',
    y = '% Change'
).properties(
    title='Top 10 Negative percentage changes for the Stock'
)
    
st.header("Does Percentage Changes history mean something?")
st.caption("The first two juxtaposed visualizations are for top 10 positive and top 10 negative percentage changes in last 5 years of the stock trading history. It gives the date and amount of percentage change for a that particular date") 
st.altair_chart(top_positive | top_negative)

st.caption("Here, we plot percentage changes historical trend and compare with its frequency of occurence. Also, you can adjust the slider to see info about specific range of percentage fluctationn. This helps to understand about volatility of stocks and unravel hidden patterns about stock price fluctation pattern.")
#df

#pip install streamlit


pct_range = st.slider('% Change',
                    min_value=int(df['% Change'].min()),
                    max_value=int(df['% Change'].max()),
                    value=(int(df['% Change'].min()), int(df['% Change'].max())))

def get_slice_membership(df, pct_range): 
    labels = pd.Series([1] * len(df), index=df.index)
    if pct_range is not None:
        labels &= df['% Change'] >= pct_range[0]
        labels &= df['% Change'] <= pct_range[1]
    return labels

slice_labels = get_slice_membership(df, pct_range)

pct_change_slice = df[slice_labels]

chart = alt.Chart(pct_change_slice, title='In Slice').mark_bar(tooltip=True).encode(
    alt.X('% Change', bin=alt.Bin(step=1)),
    alt.Y('count()')
).interactive()


st.altair_chart(chart, use_container_width=True)

st.title("Does History repeat itself?")
st.caption("This is the life time interactive price curve for the stock. Please feel free to zoom and interact with the graph to see if there is any repeating pattern in here. Do we think historical data of the price repeats after a certain period of time. Also, we render critical metrics to support this graph such as real-time price of the stock, percentage change in price and 52 week price trend of the stock. The output of price is in the currency the stock is traded in such as USD, EUR etc. ")
start = pd.to_datetime(['1970-01-01']).astype(int)[0]//10**9
end = pd.to_datetime(['today']).astype(int)[0]//10**9
# end = pd.to_datetime(['2020-12-31']).astype(int)[0]//10**9 # convert to unix timestamp.
url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock_ticker + '?period1=' + str(start) + '&period2=' + str(end) + '&interval=1d&events=history'
df2 = pd.read_csv(url)


scatter = alt.Chart(df2,width=700).mark_line(
    tooltip=True
).encode(
    alt.X('Date:T', scale=alt.Scale(zero=False)),
    alt.Y("Adj Close", scale=alt.Scale(zero=False)),
).interactive()

st.altair_chart(scatter)

tickerData = yf.Ticker(stock_ticker)

last_pct_change = str(df['% Change'].iloc[-1]) + "%"
col1, col2, col3 = st.columns(3)
col1.metric("Current Trading Price"+' (In '+tickerData.info.get('currency') + ')', tickerData.info.get('currentPrice'), last_pct_change)
code_color = "normal"
if((tickerData.info.get('recommendationMean')>2) and (tickerData.info.get('recommendationMean')<3)):
    code_color="off"
analyst_rating = tickerData.info.get('recommendationMean')
col2.metric("Analyst Rating", tickerData.info.get('recommendationKey'), analyst_rating, code_color)
col3.metric("52 week Average Price "+' (In '+tickerData.info.get('currency') + ')', tickerData.info.get('fiftyDayAverage'), tickerData.info.get('52WeekChange'))
#st.metric(label="Current Trading Price"+' (In '+tickerData.info.get('currency') + ')', value=tickerData.info.get('currentPrice'), delta=last_pct_change, delta_color="normal")




st.markdown("This project was created by Urvish Thakkar and Princy Sasapara for the Interactive Data Science(https://dig.cmu.edu/ids2022) course at Carnegie Mellon University (https://www.cmu.edu).")
