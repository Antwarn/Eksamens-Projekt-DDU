import streamlit as st
import matplotlib.pyplot as plt
import csv
import mpld3
import streamlit.components.v1 as components
from mpld3 import plugins
import pandas as pd
import numpy as np

def display_netflix():
    with open('stockinfo.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []
        line_number = 0

        for row in csv_reader:
            if line_number % 6 == 2:
                time = row[0]
                price = row[2]
                volume = row[3]
                mc = row[4]
                point = [time, price, volume, mc]
                data.append(point)
            line_number += 1


    price = [float(i[1]) for i in data]
    time = [i[0] for i in data]

    plot = plt.figure(figsize=(7,5))

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
            for x, y in xy_data:
                html_label = f'<table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> </thead> <tbody> <tr> <th>x</th> <td>{x}</td> </tr> <tr> <th>y</th> <td>{y}</td> </tr> </tbody> </table>'
                labels.append(html_label)
            tooltip = plugins.PointHTMLTooltip(line, labels, css=css)
            plugins.connect(plot, tooltip)
    
    fig_html = mpld3.fig_to_html(plot)
    components.html(fig_html, height=600)