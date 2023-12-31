import os
import yfinance as yf
import json
from datetime import datetime
import pandas as pd
import sqlite3

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")  # Fetch data for the past day
    return data

def save_stock_data(data, symbol):
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d")

    # Save as folder
    folder_path = os.path.join(symbol, current_time)
    os.makedirs(folder_path, exist_ok=True)
    data.to_csv(os.path.join(folder_path, "data.csv"))

if __name__ == "__main__":
    symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]  # Add more symbols as needed
    for symbol in symbols:
        data = fetch_stock_data(symbol)
        save_stock_data(data, symbol)
