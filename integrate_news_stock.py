import yfinance as yf
import pandas as pd
import datetime as dt


def fetch_stock_news(ticker="GOOGL", start="2023-01-01", end="2024-01-01", news_csv="news_sentiment.csv"):
    # Get stock information directly fromYahoo Finance
    stock_data = yf.download(ticker, start=start, end=end)
    stock_data.reset_index(inplace=True)

    # Load news
    news_df = pd.read_csv(news_csv)
    news_df["date"] = pd.to_datetime(news_df["date"])

    # Aggregate data using date as key
    stock_data["Date"] = pd.to_datetime(stock_data["Date"])
    merged_df = pd.merge(stock_data, news_df, left_on="Date", right_on="date", how="left")

    # Replace the missing news with Sentiment Score = 0
    merged_df["sentiment_score"].fillna(0, inplace=True)

    print("✅ Successfully retrieve stock data + news!")
    return merged_df


if __name__ == "__main__":
    df = fetch_stock_news()
    print(df.head())  # Show example
