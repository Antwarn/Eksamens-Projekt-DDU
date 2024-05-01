import pandas as pd

def change():
    df = pd.read_csv('stockinfo.csv')
    prev_price = None
    for index, row in df.iterrows():
        if (index + 1) % 6 == 2:  # If it's every sixth line
            if prev_price is not None:
                current_price = float(row[2])  # Assuming the price is in the third column
                price_change = current_price - prev_price
                print(f"Change from line {index-5} to {index+1}: {price_change}")
            prev_price = float(row[2])  # Assuming the price is in the third column

change()
