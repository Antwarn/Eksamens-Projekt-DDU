import csv
import pandas as pd

# Define a function to calculate the price change and write to a CSV file

def calculate_change(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        lines = [row for row in csv_reader]  # Read all lines into a list

        with open('price_changes.csv', 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(["Price Change", "Percent Change"])  # Corrected header row
            
            for start_line in range(len(lines) - 6):  # Loop through each starting line
                start_price = float(lines[start_line][2])  # Assuming the price is in the second column
                end_price = float(lines[start_line + 6][2])  # Get the price 6 lines ahead
                price_change = end_price - start_price
                percent_change = (price_change / start_price) * 100
                csv_writer.writerow([price_change, percent_change])  # Write to CSV file

# Call the function to execute
calculate_change('stockinfo.csv')

# Read both CSV files into DataFrames
df1 = pd.read_csv('stockinfo.csv')
df2 = pd.read_csv('price_changes.csv')

# Merge the DataFrames
merged_df = pd.concat([df1, df2], axis=1)

# Print or do further operations with the merged DataFrame
print(merged_df)

merged_df.to_csv('merged_stockinfo.csv', index=False)