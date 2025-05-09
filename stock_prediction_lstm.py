import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load stock information
def load_stock_data(filename="AAPL_data.csv"):
    df = pd.read_csv(filename)

    # Verify that the column "Close" are there non-numeric values?
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")  # convert to numbers If the error is NaN
    df.dropna(inplace=True)  # Delete rows containing NaN

    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df


# Prepare data for LSTM
def prepare_data(df, time_steps=30):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df[["Close"]])

    X, y = [], []
    for i in range(time_steps, len(scaled_data)):
        X.append(scaled_data[i-time_steps:i])
        y.append(scaled_data[i])

    X, y = np.array(X), np.array(y)
    return X, y, scaler

# Create a model LSTM
def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

if __name__ == "__main__":
    # Load and prepare data
    df = load_stock_data()
    X, y, scaler = prepare_data(df)

    # Create a model
    model = build_lstm_model((X.shape[1], 1))

    # Train model
    model.fit(X, y, epochs=10, batch_size=16, validation_split=0.2)

    # Save model
    model.save("lstm_stock_model.h5")
    print("✅ Save model lstm_stock_model.h5 succeed!")

