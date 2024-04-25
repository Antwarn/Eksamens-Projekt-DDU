import pandas as pd
import os
import re

input_file = 'stockinfo (5).csv'
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
    # Remove spaces and special characters from company name
    clean_company_name = re.sub(r'\W+', '', company_name)
    company_df = df[df['company'] == company_name]
    company_df.to_csv(f'{output_folder}/{clean_company_name}.csv', index=False)
