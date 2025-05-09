import requests
import pandas as pd

def fetch_news():
    api_key = "NEWS_API_KEY"  #API Key
    url = ("https://newsapi.org/v2/everything?"
           "q=stock market&"
           "language=en&"
           "sortBy=publishedAt&"
           f"apiKey={api_key}")

    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get("articles", [])

    news_list = []
    for article in articles:
        news_list.append({
            "date": article["publishedAt"][:10],  #pull only date
            "headline": article["title"],
            "link": article["url"]
        })

    df = pd.DataFrame(news_list)
    df.to_csv("news_data.csv", index=False)
    print("✅ Save news to file news_data.csv complete!")

if __name__ == "__main__":
    fetch_news()
