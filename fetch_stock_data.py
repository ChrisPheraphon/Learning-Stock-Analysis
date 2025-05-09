import yfinance as yf
import pandas as pd


def get_stock_data(ticker, start="2022-01-01", end="2024-01-01"):
    stock = yf.download(ticker, start=start, end=end)

    # Reset the index so that Date is the column.
    stock.reset_index(inplace=True)

    # Select only the desired columns.
    stock = stock[["Date", "Close"]]

    # Save CSV
    stock.to_csv(f"{ticker}_data.csv", index=False)
    print(f"✅ Save {ticker}_data.csv succeed!")


if __name__ == "__main__":
    get_stock_data("AAPL")  # Retrieve stock information Apple
