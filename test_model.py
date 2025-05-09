import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load the trained model.
model = tf.keras.models.load_model("lstm_stock_model.h5")

# Load stock information
def load_stock_data(filename="AAPL_data.csv"):
    df = pd.read_csv(filename)
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df.dropna(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df

# Prepare data for testing
def prepare_test_data(df, scaler, time_steps=30):
    scaled_data = scaler.transform(df[["Close"]])
    input_data = scaled_data[-time_steps:].reshape(1, time_steps, 1)
    return input_data

if __name__ == "__main__":
    df = load_stock_data()

    # Create scaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit(df[["Close"]])

    # Prepare input for prediction
    input_data = prepare_test_data(df, scaler)

    # Predict the next day's stock price
    predicted_price = model.predict(input_data)
    predicted_price_inv = scaler.inverse_transform(predicted_price)

    print(f"📈 Predict the next day's stock price: {predicted_price_inv[0][0]:.2f} USD")

    # Plot last 30 days actual prices + predicted next day
    last_30_days = df["Close"].tail(30).tolist()
    predicted_day = [predicted_price_inv[0][0]]

    # Create timeline for plotting
    dates = df.tail(30).index.tolist()
    dates.append(dates[-1] + pd.Timedelta(days=1))

    prices = last_30_days + predicted_day

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(dates[:-1], last_30_days, label="Actual Price", marker='o')
    plt.plot(dates[-2:], prices[-2:], label="Predicted Price", color="red", marker='x', linestyle='--')
    plt.xticks(rotation=45)
    plt.title("Stock Price Prediction (Next Day)")
    plt.xlabel("Date")
    plt.ylabel("Stock Close Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
