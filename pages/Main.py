import yfinance as yf
import streamlit as st

from Hjem import display_hjem
from AMD import display_AMD
from Netflix import display_netflix
from Microsoft import display_micro
from Apple import display_apple
from Ralph import display_ralph
from Google import display_google
from nvidia import display_nvidia
# Sidebar navigation    
page = st.sidebar.radio("Navigation", ["Hjem", "AMD", "Netflix", "Microsoft", "Apple", "Ralph Lauren", "Google", "Nvidia"])

# Display different content based on the selected page
if page == "Hjem":
    display_hjem()
elif page == "AMD":
    display_AMD()
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

    


#tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
#tab1.write("this is tab 1")
#tab2.write("this is tab 2")