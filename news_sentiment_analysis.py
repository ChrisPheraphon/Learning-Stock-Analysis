from transformers import pipeline
import pandas as pd

# Load the analysis model Sentiment
sentiment_pipeline = pipeline("sentiment-analysis")


def analyze_news_sentiment(news_csv="news_data.csv"):
    df = pd.read_csv(news_csv)

    sentiment_results = []
    for index, row in df.iterrows():
        sentiment = sentiment_pipeline(row["headline"])
        sentiment_score = sentiment[0]["score"] if sentiment[0]["label"] == "POSITIVE" else -sentiment[0]["score"]
        sentiment_results.append({
            "date": row["date"],
            "headline": row["headline"],
            "sentiment_score": sentiment_score
        })

    sentiment_df = pd.DataFrame(sentiment_results)
    sentiment_df.to_csv("news_sentiment.csv", index=False)
    print("✅ Save results to file news_sentiment.csv สำเร็จ!")


if __name__ == "__main__":
    analyze_news_sentiment()
