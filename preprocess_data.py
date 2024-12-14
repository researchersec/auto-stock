import os
import pandas as pd
import json

def preprocess_data(base_path, output_file="stock_data.json"):
    symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]  # Add more symbols as needed
    all_data = {}

    for symbol in symbols:
        # Adjust file path based on your structure
        file_path = os.path.join(base_path, f"{symbol}/2023-09-25_01-05-05/data.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path, parse_dates=["Date"])
            df = df[["Date", "Close"]]  # Include other columns if needed
            all_data[symbol] = {
                "dates": df["Date"].dt.strftime("%Y-%m-%d").tolist(),
                "close": df["Close"].tolist(),
            }
        else:
            print(f"File not found: {file_path}")

    # Save all data to JSON
    with open(output_file, "w") as f:
        json.dump(all_data, f, indent=4)
    print(f"Data saved to {output_file}")

# Run preprocessing
preprocess_data("./data")
