import os
import pandas as pd
import json

def preprocess_data(base_path, output_file="stock_data.json"):
    symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]  # Add more symbols as needed
    all_data = {}

    for symbol in symbols:
        # Define the symbol's base folder
        symbol_path = os.path.join(base_path, symbol)
        print(f"Checking symbol folder: {symbol_path}")
        
        if not os.path.exists(symbol_path):
            print(f"Symbol folder not found: {symbol_path}")
            continue

        # Gather all subdirectories
        subdirs = [os.path.join(symbol_path, d) for d in os.listdir(symbol_path) if os.path.isdir(os.path.join(symbol_path, d))]
        print(f"Found subdirectories: {subdirs}")
        
        if not subdirs:
            print(f"No subdirectories found for symbol: {symbol}")
            continue

        # Initialize an empty DataFrame to aggregate data
        combined_data = pd.DataFrame()

        for subdir in subdirs:
            file_path = os.path.join(subdir, "data.csv")
            print(f"Looking for file: {file_path}")
            
            if os.path.exists(file_path):
                print(f"Processing file: {file_path}")
                # Read and process the CSV file
                df = pd.read_csv(file_path, parse_dates=["Date"])
                df = df[["Date", "Close"]]  # Include other columns if needed
                combined_data = pd.concat([combined_data, df])

        # Sort and remove duplicate dates
        if not combined_data.empty:
            combined_data = combined_data.sort_values("Date").drop_duplicates(subset="Date")

            all_data[symbol] = {
                "dates": combined_data["Date"].dt.strftime("%Y-%m-%d").tolist(),
                "close": combined_data["Close"].tolist(),
            }

    # Save all data to JSON
    with open(output_file, "w") as f:
        json.dump(all_data, f, indent=4)
    print(f"Data saved to {output_file}")

# Run preprocessing
preprocess_data("")
