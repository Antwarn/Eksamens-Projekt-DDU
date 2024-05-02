import streamlit as st
import matplotlib.pyplot as plt
import csv
import mpld3
import streamlit.components.v1 as components
from mpld3 import plugins
import pandas as pd
import numpy as np

def filter_rows(rows):
    filtered_rows = []
    for row in rows:
        time = row[0][-8:]
        if '15:30' <= time <= '22:00':
            filtered_rows.append(row)
    return filtered_rows

def display_apple():
    with open('stockinfo_5.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []
        line_number = 5

        for row in csv_reader:
            if line_number % 6 == 1:
                time = row[0]
                opn = row[2]
                high = row[3]
                low = row[4]
                price = row[5]
                close = row[6]
                volume = row[7]
                point = [time, price,opn,high,low,close,volume]
                data.append(point)
            line_number += 1
    
    # Fjern uønskede rækker baseret på klokkeslæt
    filtered_data = filter_rows(data)

    price = [float(i[1]) for i in filtered_data]
    time = [i[0] for i in filtered_data]
    opn = [float(i[2]) for i in filtered_data]
    high = [float(i[3]) for i in filtered_data]
    low = [float(i[4]) for i in filtered_data]
    close = [float(i[5]) for i in filtered_data]
    volume = [float(i[6]) for i in filtered_data]

    plot = plt.figure(figsize=(7,7))

    plt.plot(time, price, color='tab:orange', linestyle='solid', marker='.')

    css = """
    table
    {
        border-collapse: collapse;
    }
    th
    {
        color: #ffffff;
        background-color: #000000;
    }
    td
    {
        background-color: #cccccc;
    }
    table, th, td
    {
        font-family:Arial, Helvetica, sans-serif;
        border: 1px solid black;
        text-align: right;
    }
    """

    for axes in plot.axes:
        for line in axes.get_lines():
            xy_data = line.get_xydata()
            labels = []
            i = 0
            for x, y in xy_data:
                html_label = f'<table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> </thead> <tbody> <tr> <th>Time</th> <td>{time[i]}</td> </tr> <tr> <th>Price</th> <td>${y}</td> </tr> <tr> <th>Open</th> <td>${opn[i]}</td> </tr> <tr> <th>High</th> <td>${high[i]}</td> </tr><tr> <th>Low</th> <td>${low[i]}</td> </tr><tr> <th>Close</th> <td>${close[i]}</td> </tr> <tr> <th>Volume</th> <td>{volume[i]}</td> </tr> </tbody> </table>'
                labels.append(html_label)
                i = i+1
            tooltip = plugins.PointHTMLTooltip(line, labels, css=css)
            plugins.connect(plot, tooltip)
    
    fig_html = mpld3.fig_to_html(plot)
    components.html(fig_html, width=800, height=800)

    # Gem de filtrerede rækker i en ny CSV-fil
    with open('ny_stockinfo.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(filtered_data)

