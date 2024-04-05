import pandas as pd

def get_price(file_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Extract the price (assuming it's in the first row, third column)
    price = df.iloc[0, 2]  # Assuming price is in the first row, third column

    # Convert price to float
    price = float(price)

    return price

# Example usage:
csv_file = "stockinfo.csv"

# Store the price in a variable called 'change'
change = get_price(csv_file)

# Print the type of the variable
print("Type of 'change':", type(change))

# Print the price
print("Price:", change)
