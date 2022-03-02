# Stonkers



## Project Goals

**Major Goal:** Explore historical stock return trends
**Research Questions:
**
1. Has the crypto volatility affected other stock returns? - Have these new highly volatile investment options, and the ever-changing crypto investment policies of different governments affected the returns of traditional stocks?
2. Is there any pattern or trend when the 10 biggest movements happened in the particular stock - "History repeats itself" is a highly used phrase in the stock market world, how well does it hold, and is it true.


## Design

We started by sketching some visualizations on paper based on our data and research question. We started creating paper prototypes for different graphs and possible interactions and then modified some visuals based on our coding capabilities.
**Overview based on research questions:

**Has the crypto volatility affected other stock returns?”** - to address this question we started to brainstorm ways in which we could compare the price of stocks with cryptocurrencies, and also with each other to see who was affected the most
     Possible plots that we brainstormed:  
            Correlation Plots
            Bar charts for returns
            Time-series graphs
 1. With the first visualization, we wanted to give an overview of the change in returns for the stocks that the users select for the time frame.
      **Interactions:** When the user selects the stocks from the dropdown, the graph automatically updates to show the returns for the selected stocks
 2. To really utilize the power of Altair, we combined the time series chart that shows returns for all stocks and crypto, with a bar chart that shows average           return for the selected time frame.
      ** Interactions:** 1. When the user selects a time frame on the time-series graph, the bar chart updates to show the average return for that specific time         frame. 2. When the user slides the selection, it shows the change in average return in the bar chart.

**“Is there any pattern or trend when the 10 biggest movements happened in the particular stock” **

We had some domain knowledge as we personally belong to families who have been into stock market trading for more than the past 25 years. Thus, we intuitively and utilizing our domain knowledge started building visualizations that we thought might have some insights and might be useful. The domain knowledge helped us in deciding the parameters we should focus on while creating visualizations. In the process, we built some really insightful visualizations which unraveled a lot of information and hidden trends. Thus, while choosing our final set of visualizations we kept the visualizations most associated with each other and that really discovered some pattern or told a really good story/insight.   




## Development

After deciding upon a common goal, and deciding upon our research questions, we brainstormed some possible visualization together. 
We then picked one research question each and diverged to develop these visualizations we decided upon. 
The development process was more iterative than we had planned. A couple of times, due to our coding limitations, we were unsuccessful in creating a visualization that we initially planned to, and sketched new ones based on feasibility. 
We are using finance library to fetch data dynamically.
**Total time spent:** ~45 hours combined
**Most time consuming aspects:** Overcoming roadblocks like issues in setting up the environment and debugging, iterating during development because certain visualizations didn’t go as planned. 



## Success Story

We built and intuitive as well as well thought visualizations using the domain knowledge we had. From our visualizations, we were able to discover a unique quality about daily percentage changes. 

Key insights and discoveries addressing our questions:

**“Has the crypto volatility affected other stock returns?” **

     - Contrary to the popular belief, the crypto volatility hasn’t shown significant affect on stock returns. In our interaction with the bar chart and time series        graphs, some stocks showed positive correlation with crypto returns while some showed negative.
     - It was a success to be able to see in a visually clear manner, how the average of returns changed for each stock option over time.


**“ Is there any pattern or trend when the 10 biggest movements happened in the particular stock”**
     We observed that most of the daily percentage changes are in the range of -1 to 1. When the frequency of percentage changes is plotted against its count, we observe that it almost looks like a normal distribution and the plot assumes a shape like a bell curve which is centered at 0. This was true for almost all of the stocks. 
     This is a very critical point to be considered while doing intraday trading. As, to make profits while intraday trading you should be very selective about which stock you are selecting because the majority of the time the stock price is not going to change very much in a single day. 
     That being said, in another of our visualizations where we plot top 10 percentage changes in the last 5 years we observed that sometimes there were changes as high as 58% on one single day. Thus, if correct strategies, domain expertise, and strong analysis of the scenario is done, a huge amount of profits can be made by intraday trading as well. 
     Also, when one analyses the top 10 positive percentage change and top 10 negative percentage change trends it is observed that this high fluctuation happen on days like when the company’s earnings were announced, some global phenomenon happen such as Covid-19 declared as a global pandemic, election results are announced among others or there was major news related to the company such as ‘CEO steps down, ‘their product got an approval/certification by some authority’, etc. So, these high fluctuations were basically a quick reaction to company-related sentiments rather than some solid change in business metrics. We demystified stock market fluctuations and we felt our visualizations we're able to give significant insights about stock prices percentage changes.     
