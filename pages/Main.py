import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from Hjem import display_hjem
from Netflix import display_netflix
from Microsoft import display_micro
from Apple import display_apple
from Ralph import display_ralph
from Google import display_google
from nvidia import display_nvidia









# Sidebar navigation    
page = st.sidebar.radio("Navigation", ["Hjem", "Netflix", "Microsoft", "Apple", "Ralph Lauren", "Google", "Nvidia"])

# Display different content based on the selected page
if page == "Hjem":
    display_hjem()
elif page == "Netflix":
    display_netflix()
elif page == "Microsoft":
    display_micro()
elif page == "Apple":
    display_apple()
elif page == "Ralph Lauren":
    display_ralph()
elif page == "Google":
    display_google()
elif page == "Nvidia":
    display_nvidia()

