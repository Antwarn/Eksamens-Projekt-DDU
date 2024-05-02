import streamlit as st
import matplotlib.pyplot as plt
import csv
import mpld3
import streamlit.components.v1 as components



def display_micro():
    
    with open('stockinfo.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []
        line_number = 0

        for row in csv_reader:
            if line_number % 6 == 0:
                time = row[0]
                price = row[2]
                volume = row[3]
                mc = row[4]
                point = [time, price, volume, mc]
                data.append(point)
            line_number += 1

    price = [float(i[1]) for i in data]
    time = [i[0] for i in data]


    fig = plt.figure()
    plt.plot(time, price)

    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)
