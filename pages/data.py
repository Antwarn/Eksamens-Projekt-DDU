import csv
import pandas




with open('stockinfo_navne.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        price = row[2]
        volume = row[3]
        mc = row[4]
        print(price, volume, mc)


