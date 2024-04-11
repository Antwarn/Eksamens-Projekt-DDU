import csv
import pandas




with open('stockinfo.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    data = []

    line_number = 0

    for row in csv_reader:
        line_number += 1
        if line_number % 6 == 0:
        
            price = row[2]
            volume = row[3]
            mc = row[4]
            x = [price, volume, mc]
            data.append(x)

    print(data)
