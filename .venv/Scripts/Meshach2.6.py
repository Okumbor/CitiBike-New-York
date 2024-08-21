################################################ CITI BIKES DASHBOARD #####################################################

import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt

########################### Initial settings for the dashboard ##################################################################


st.set_page_config(page_title = 'Citi Bikes Dashboard', 
                   layout='wide',     
                   initial_sidebar_state="expanded"
                   )
st.title("Citi Bikes Dashboard")
st.markdown("The dashboard will help with the problems CitiBikes are currently facing")
st.markdown("Right now, Citi Bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")

########################## Import data ###########################################################################################
path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\Scripts\reduced_data_to_plot.csv"
df = pd.read_csv(path, index_col = 0)
path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\Scripts\top20.csv"
top20 = pd.read_csv(path, index_col = 0)

# ######################################### CREATE THE CHARTS #####################################################################

## Bar chart

# top20 is the DataFrame with the top 20 stations.
fig = go.Figure(go.Bar(x=top20['start_station_name'], y = top20['value'], marker={'color': top20['value'],'colorscale': 'Blues'}))

# Update the layout to add a title and ensure adequate margin space.
fig.update_layout(
    title='Top 20 Popular Bike Stations in New York',
    xaxis_title='Station Name',
    yaxis_title='Sum of Trips',
    width = 900, height = 600,
    margin=dict(l=40, r=40, t=40, b=100)  # Adjust margins to ensure no clipping
)

st.plotly_chart(fig, use_container_width=True)

## Dual Line Chart

# Create a figure with secondary y-axis configuration
fig2 = make_subplots(specs=[[{"secondary_y": True}]])
# Add bike rides daily data trace
fig2.add_trace(
    go.Scatter(x=df['date'], y=df['bike_trips_daily'], name='Daily Bike Rides', marker_color='red'),
    secondary_y=False,  # False indicates this trace uses the left y-axis
)
# Add average temperature data trace
fig2.add_trace(
    go.Scatter(x=df['date'], y=df['temp_avg'], name='Daily Temperature', marker_color='blue'),
    secondary_y=True,  # True indicates this trace uses the right y-axis
)
# Set x-axis title
fig2.update_xaxes(title_text='Date')
# Set y-axes titles
fig2.update_yaxes(title_text='Bike Rides Daily', secondary_y=False)
fig2.update_yaxes(title_text='Average Temperature (°C)', secondary_y=True, tickfont_color='blue')
# Add a title to the plot
fig2.update_layout(
    title='Daily Bike Rides and Temperature in 2022',
    showlegend=True
)
st.plotly_chart(fig2, use_container_width=True)

### Add the kepler.gl map ###
# correct path to the file
path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\Scripts\New_York CitiBike Trips Aggregated.html"

# Read the file and store its contents in a variable
with open(path, 'r', encoding='utf-8') as f:
    html_data = f.read()


## Show in HTML content in Streamlit
st.header("Aggregated CitiBike Trips in New York")
st.components.v1.html(html_data,height=1000)


