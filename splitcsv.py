import pandas as pd
import os

input_file = 'stockinfo.csv'
output_folder = 'output'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the input CSV file
df = pd.read_csv(input_file)

# Get unique company names
unique_companies = df['company'].unique()

# Write separate CSV files for each company
for company_name in unique_companies:
    company_df = df[df['company'] == company_name]
    company_df.to_csv(f'{output_folder}/{company_name}.csv', index=False)
