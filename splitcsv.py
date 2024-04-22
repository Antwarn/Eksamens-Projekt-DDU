import pandas as pd

input_file = 'stockinfo.csv'
output_folder = 'output'

# Create output folder if it doesn't exist
import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the input CSV file
df = pd.read_csv(input_file)

# Set the number of companies here
num_companies = 6

# Split the data into separate dataframes based on company ID
company_dfs = [df[df['company'] == i] for i in range(num_companies)]

# Write the output CSV files
for i, company_df in enumerate(company_dfs):
    company_df.to_csv(f'{output_folder}/company_{i}.csv', index=False)