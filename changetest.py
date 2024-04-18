import pandas as pd

# Load the data into a Pandas DataFrame
df = pd.read_csv('stockinfo.csv')

# Calculate the change in company price from the previous line
df['company_price_change'] = df['company_price'] - df['company_price'].shift(1)

# If necessary, fill the missing values caused by the first row (no previous row)
df['company_price_change'].fillna(0, inplace=True)