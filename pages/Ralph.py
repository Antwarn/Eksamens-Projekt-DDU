import streamlit as st
import matplotlib.pyplot as plt
import csv
import mpld3
import streamlit.components.v1 as components
from mpld3 import plugins
import pandas as pd
import numpy as np

def display_ralph():
    with open('stockinfo.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []
        line_number = 0

        for row in csv_reader:
            if line_number % 6 == 3:
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
    fig_html = mpld3.fig_to_html(plot)
    components.html(fig_html, width=800, height=800)