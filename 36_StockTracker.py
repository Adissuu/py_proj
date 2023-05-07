import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_KEY = "97LL084MJ44E6HNN"
NEWS_KEY = "9def7aca7366472e91cbf98c99771cdd"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_price = day_before_yesterday["4. close"]

difference = float(yesterday_price) - float(day_before_yesterday_price)
diff_percent = (difference / float(yesterday_price)) * 100

if diff_percent > 5 or diff_percent < -5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_KEY,
    }

    q_res = requests.get(NEW_ENDPOINT, params=news_params)
    articles = q_res.json()["articles"]

    articles = articles[:3]

    formatted_articles = [ f"Headline: {article['title']}\n\nBrief: {article['description']}"for article in articles]

    print(formatted_articles)