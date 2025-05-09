# 📈 Stock Price Prediction with LSTM and News Sentiment (Apple Inc.)

This project demonstrates how to predict stock prices for **Apple Inc. (AAPL)** using **historical price data** and **news sentiment analysis**, applying **LSTM (Long Short-Term Memory)** deep learning models.

---

## 🔍 Project Overview

The goal is to investigate whether combining **stock historical data** and **news sentiment** can improve the accuracy of predicting stock price trends.

---

## 🛠 Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- yfinance
- scikit-learn
- python-dotenv

---

## 🗂 File Overview

| File | Description |
|------|-------------|
| `fetch_stock_data.py` | Fetches historical stock prices from Yahoo Finance |
| `fetch_news_data.py` | Downloads and preprocesses news headlines (uses API key) |
| `news_sentiment_analysis.py` | Converts news headlines into sentiment scores |
| `integrate_news_stock.py` | Merges stock and sentiment data |
| `stock_prediction_lstm.py` | Builds and trains the LSTM model |
| `test_model.py` | Evaluates the model's predictions |
| `.env` | Stores API keys (not tracked in Git) |

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add your API key:

Ensure `.env` is added to your `.gitignore` file to prevent accidental uploads.

---

## 🧪 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt


