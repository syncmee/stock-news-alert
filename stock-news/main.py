import pandas as pd
import requests
import newsapi
from pandas import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
news_api = "$$$ Your News API Key $$$"
stock_api = "$$$ Your Stock API Key $$$"
news = {
    "q": COMPANY_NAME,
    "from": "2024-06-09",
    "to": "2024-06-10",
    "domains": "bbc.co.us, reuters.com, cnbc.com, ft.com",
    "apiKey": news_api,
    "language": "en",

}

news_daily = requests.get(url="https://newsapi.org/v2/everything", params=news)
stock_news = news_daily.json()
news1 = (f"TSLA: 🔺2% \n"
         f"Headline :{stock_news['articles'][0]['description']}")
news2 = f"Headline :{stock_news['articles'][1]['description']}"
news3 = f"Headline :{stock_news['articles'][2]['description']}"

stock_daily = requests.get(
    url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol=TSLA&datatype=csv&apikey={stock_api}")
content = stock_daily.text
# with open(file="stock_prices.csv", mode="") as stock_prices:
#     stock_prices.write(content)

data = pd.read_csv("stock_prices.csv")
close_price = data.close.to_list()
open_price = data.open.to_list()

close_yesterday = close_price[0]
close_day_before_yesterday = close_price[1]
percentage_change = round(((close_yesterday - close_day_before_yesterday) / close_day_before_yesterday) * 100, 2)


def check_integer(num):
    global rohit
    if num > 0:
        rohit = news1.replace("🔻", "🔺").replace("2", str(percentage_change))
    elif num < 0:
        rohit = news1.replace("🔺", "🔻").replace("2", str(percentage_change))


check_integer(percentage_change)
news_list = [rohit, news2, news3]

for n in news_list:
    print(n)

## STEP 3: Use https://www.twilio.com

# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
