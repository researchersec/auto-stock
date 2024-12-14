import os
import pandas as pd
import json

def preprocess_data(base_path, output_file="stock_data.json"):
    symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]  # Add more symbols as needed
    all_data = {}

    for symbol in symbols:
        # Define the symbol's base folder
        symbol_path = os.path.join(base_path, symbol)
        
        # Check if the symbol folder exists
        if not os.path.exists(symbol_path):
            print(f"Symbol folder not found: {symbol_path}")
            continue

        # Find the latest subdirectory (by timestamp in its name)
        subdirs = [os.path.join(symbol_path, d) for d in os.listdir(symbol_path) if os.path.isdir(os.path.join(symbol_path, d))]
        if not subdirs:
            print(f"No subdirectories found for symbol: {symbol}")
            continue

        latest_subdir = max(subdirs, key=os.path.getmtime)  # Get the most recently modified folder
        file_path = os.path.join(latest_subdir, "data.csv")
        
        # Check if the data.csv file exists
        if os.path.exists(file_path):
            # Read and process the CSV file
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
