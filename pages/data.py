import csv
import pandas
import matplotlib as mp



def datalist():
    with open('stockinfo.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []

        line_number = 0

        for row in csv_reader:
            if line_number % 6 == 0:
            
                price = row[2]
                volume = row[3]
                mc = row[4]
                x = [price, volume, mc]
                data.append(x)
            line_number += 1

        print(data)


import csv

def calculate_change(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        lines = [row for row in csv_reader]  # Read all lines into a list

        with open('price_changes.csv', 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(["Price Change", "Procent change"])  # Write header row
            
            for start_line in range(len(lines) - 6):  # Loop through each starting line
                start_price = float(lines[start_line][2])  # Assuming the price is in the second column
                end_price = float(lines[start_line + 6][2])  # Get the price 6 lines ahead
                price_change = end_price - start_price
                pro_change = (price_change/end_price)*100
                csv_writer.writerow([price_change, pro_change])  # Write to CSV file

# Call the function to execute
calculate_change('stockinfo.csv')


