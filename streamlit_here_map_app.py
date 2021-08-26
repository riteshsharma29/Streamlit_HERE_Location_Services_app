import requests
import streamlit.components.v1 as components
from urllib.request import urlopen
import json
import streamlit as st
import pyautogui

clear = st.sidebar.button("CLEAR")
location = st.sidebar.text_input("Enter Location ","")

def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)
    pyautogui.press("return", interval=0.15)

# Clear location
if clear:
    Clear()

st.title("**" + "Sreamlit - HERE Location Services app" + "**")

@st.cache(allow_output_mutation=True)
def get_longitude_latitude(location):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'UPDATE-YOUR-JAVASCRIPT-API-KEY'  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']

    # Read in the file
    with open('source.js', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('latval', str(latitude))
    filedata = filedata.replace('lngval', str(longitude))
    filedata = filedata.replace('rndlat', str(latitude).split(".")[0])
    filedata = filedata.replace('rndlng', str(longitude).split(".")[0])

    # Write the file out again
    with open('C:\\xampp\\htdocs\\demo.js', 'w') as file:
        file.write(filedata)


if len(location) > 1:
    try:
        get_longitude_latitude(location)
        st.markdown("**" + location.upper() + "**")
        components.iframe("http://localhost/demo.html",width=900,height=1200)
    except:
        st.error("Invalid Location")
