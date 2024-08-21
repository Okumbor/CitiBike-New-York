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
from numerize.numerize import numerize
from PIL import Image

########################### Initial settings for the dashboard ##################################################################

st.set_page_config(
                   page_title = 'Citi Bikes Strategy Dashboard', 
                   layout='wide', 
                   initial_sidebar_state="expanded"
                   )

st.title("Citi Bikes Strategy Dashboard")

# Define side bar
st.sidebar.title("Selector Menu")
page = st.sidebar.selectbox('Select an aspect of the analysis',
  [ "Intro page",
    "Weather component and bike usage",
    "Most popular stations",
    "Interactive map with aggregated bike trips", 
    "Recommendations"
    ])

########################## Import data ###########################################################################################

df = pd.read_csv('reduced_data_to_plot_7.csv')
top20 = pd.read_csv('top20.csv')

# ######################################### CREATE PAGES #####################################################################

### Intro page
    
if page == "Intro page":
    st.markdown("#### Welcome to the Citi Bike Strategic Dashboard")
    st.markdown("""
    This dashboard aims to provide actionable insights into the distribution challenges Citi Bike faces in New York City. 
    Since its inception, Citi Bike has experienced a surge in demand, exacerbated by the Covid-19 pandemic, leading to 
    notable distribution issues and customer complaints about bike availability. This analysis explores potential causes 
    and proposes solutions.
    """)
    st.markdown("The dashboard is organized into the following sections:")
    st.markdown("- **Bike Station:** Visualizes the most popular stations to identify high-demand areas.")
    st.markdown("- **Weather Impact Analysis:** Examines how different weather conditions affect bike usage.")
    st.markdown("- **Trip Patterns Map:** An interactive map showing common routes and aggregated trip data.")
    st.markdown("- **Strategic Recommendations:** Offers actionable advice based on our findings to improve service availability.")
    st.markdown("Use the 'Selector Menu' dropdown menu on the left to navigate through the different aspects of our analysis.")


    path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\cITIbIKE_INTRO.jpg"
    myImage = Image.open(path) #source: https://ny.curbed.com/2020/4/14/21220752/citi-bike-coronavirus-healthcare-workers-commute
    st.image(myImage)

    ### Create the dual axis line chart page ###
    
elif page == "Weather component and bike usage":

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
    height = 400,
    showlegend=True
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("""
                
    The dual-axis line chart vividly illustrates the relationship between daily bike rides and average temperature over the year 2022. 
    Noticeably, the frequency of bike trips increases with higher temperatures, peaking during the warmer months. 
    This pattern suggests that bike usage is significantly influenced by weather conditions, 
    with more people opting to bike as temperatures become more comfortable. 
    Consequently, the drop in bike usage during colder months aligns with decreased temperatures, 
    pinpointing a seasonal trend that impacts bike availability. 
    Understanding these trends is crucial for addressing bike shortages effectively, particularly from May to October when demand is at its peak.

    The decline in bike usage during colder months can be attributed to several factors that impact the convenience and safety of biking. Key reasons include:

    - **Temperature Comfort**: Lower temperatures can significantly reduce the comfort of biking, deterring people from using bikes for their daily commutes or leisure activities.
  
    - **Safety Concerns**: Icy and snowy conditions not only make the roads slippery but also increase the risk of accidents, making biking a less appealing option during winter.

    - **Shorter Daylight Hours**: With winter days being shorter, decreased daylight hours can lead to reduced visibility, which might discourage biking, especially for commuters.

    - **Increased Sickness Rates**: The cold months often see a rise in illnesses like colds and flu, which can decrease overall physical activity levels, including biking.

    - **Availability of Alternatives**: The presence of warmer and more comfortable transportation options such as buses, subways, or cars might lead people to choose these over biking in cold weather.

    To address these challenges and encourage year-round bike usage, Citi Bike could consider initiatives 
    such as introducing seasonal pricing, enhancing bike and route safety features, 
    and promoting health benefits through collaborative campaigns. Understanding and mitigating these 
    seasonal impacts are crucial for maintaining high service availability and customer satisfaction throughout the year.
    """)


### Most popular stations page

    # Create the season variable

elif page == 'Most popular stations':
    
    # Create the filter on the side bar
    # Set up the sidebar with a multiselect widget for seasons
    with st.sidebar:
    # Ensuring that the season column exists and is populated
        if 'season' in df.columns and not df['season'].isnull().all():
            season_options = df['season'].unique()
            season_filter = st.multiselect('Select the season', options=season_options, default=season_options)
        else:
            st.error("Season data is not available in the dataset.")
            season_filter = []

    # Filter the DataFrame based on the selected seasons
    if season_filter:
        df1 = df[df['season'].isin(season_filter)]
    else:
        df1 = pd.DataFrame()  # or df1 = df to display all data when no filter is selected
    
    # Define the total rides
    total_rides = float(df1['bike_trips_daily'].count())    
    st.metric(label = 'Total Bike Rides', value= numerize(total_rides))
    
    # Bar chart
 
    df1['value'] = 1 
    df_groupby_bar = df1.groupby('start_station_name', as_index = False).agg({'value': 'sum'})
    top20 = df_groupby_bar.nlargest(20, 'value')
    
    fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker={'color':top20['value'],'colorscale': 'Blues'}))
    # Update the layout to add a title and ensure adequate margin space.
    fig.update_layout(
    title = 'Top 20 most popular bike stations in New York',
    xaxis_title = 'Start stations',
    yaxis_title ='Sum of trips',
    width = 900, height = 600,
    margin=dict(l=40, r=40, t=40, b=100)  # Adjust margins to ensure no clipping
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    This bar chart highlights the top 20 most popular Citibike stations in New York City based on the sum of trips taken from each station. 
    The station at 'Grove St PATH' emerges as the most frequented, with a significant lead over the next, 
    indicating a major hub of activity likely due to its connectivity and accessibility. 
    Following closely are 'South Waterfront Walkway' and 'Hoboken Terminal - River St', among others, which also see substantial usage.

    The disparity in usage between the most and least popular in the top 20 is pronounced, 
    with stations like 'Madison St' and '8 St & Washington St' having notably fewer trips. 
    This distribution suggests a concentration of bike usage around certain key areas, 
    which could be driven by factors such as proximity to commercial centers, residential areas, or public transit hubs.

    Understanding these patterns is crucial for effective station management and future planning, 
    particularly for addressing high-demand areas and ensuring optimal bike availability. 
    Analyzing the popularity of these stations seasonally, using the sidebar filter, 
    can further provide insights into how weather, tourist seasons, or local events influence bike-sharing usage throughout the year.
    """)

elif page == 'Interactive map with aggregated bike trips': 
    ### Add the kepler.gl map ###
    ### Create the map ###

    st.write("Interactive map showing aggregated bike trips over New York")
    # correct path to the file
    path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\Scripts\New_York CitiBike Trips Aggregated.html"
    
    # Read the file and store its contents in a variable
    with open(path, 'r', encoding='utf-8') as f:
        html_data = f.read()
   
    ## Show in HTML content in Streamlit
    st.header("Aggregated CitiBike Trips in New York")
    st.components.v1.html(html_data,height=1000)
    st.markdown("#### Using the filter on the left hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("""
                ## Observations from the Filtered Data
    ### Most Common Trips
    1. **South Waterfront Walkway - Sinatra Dr & 1 St**
        - **Trip Count**: 5439 trips
        - **Route**: The route starting and ending at South Waterfront Walkway to Sinatra Dr & 1 St is highly popular, 
        suggesting a busy local loop that is preferred for short, convenient trips within the waterfront area.

    2. **Hoboken Terminal - Hudson St & Hudson Pl to Hoboken Ave at Monmouth St**
        - **Trip Count**: 5565 trips
        - **Route**: This route connects major transit hubs and residential areas, 
        indicating its popularity among commuters and residents in Hoboken, likely due to its convenience and accessibility.

    ### Additional Observations
        - **Busy Zones**: The zones around Hoboken Terminal and South Waterfront are particularly busy. 
        These areas are key transit points and popular recreational spots, leading to higher traffic volumes.
        - **Implications**: The high frequency of trips in these areas can be attributed to the well-established cycling 
        infrastructure and the proximity to major residential and commercial hubs. This suggests that enhancing bike-related 
        facilities could further promote cycling as a convenient mode of transport.

    The filtered analysis on Kepler.gl map not only helped identify the most common trips but also provided 
    insights into urban mobility patterns in New York City. Such data can be instrumental in urban planning and improving public transportation networks.
    """)


else:
    st.header("Conclusions and Strategic Recommendations")
    # Display an illustrative image for recommendations, ensure the image path is correct or use a placeholder image
    path = r"C:\Users\okumb\Downloads\CitiBike-New-York\.venv\Bike_final.png"
    bikes = Image.open(path)  #source: https://www.flickr.com/photos/justtakenpictures/14234828797/
    st.image(bikes)

    st.markdown("""
    ### Key Insights and Future Directions:
    Our comprehensive analysis has provided valuable insights into the operational dynamics and challenges faced by Citi Bike in New York City. Here are our strategic recommendations based on the data analyzed:

    - **Enhance Station Capacity at High-Demand Locations**: 
        The data clearly shows that stations like 'Grove St PATH' and 'South Waterfront Walkway' experience very high traffic. 
        Increasing the number of docks and bikes available at these high-demand stations could alleviate some of the availability issues.

    - **Seasonal Adjustments in Bike Allocation**:
        Our analysis of bike usage against temperature trends suggests a pronounced seasonal variation in demand. 
        We recommend increasing bike availability during warmer months and reducing it in colder months to optimize resource utilization and maintenance costs.

    - **Infrastructure Improvements**:
        To support increased usage and ensure safety, upgrading biking infrastructure around popular routes and stations is crucial. 
        This includes better lighting, more bike lanes, and improved road surfaces.

    - **Targeted Marketing Campaigns**:
        Implement targeted marketing campaigns during transition seasons (spring and autumn) to encourage biking through varied weather conditions, potentially increasing off-peak usage.

    - **Developing New Stations in Emerging Hotspots**:
        By analyzing trip patterns, especially from the interactive map, potential new hotspots for station development have been identified. 
        Establishing new stations in these growing areas can cater to expanding user bases.

    ### Conclusion:
    The strategic enhancements proposed aim to bolster Citi Bike's mission of providing reliable, accessible, and enjoyable biking experiences throughout New York City. 
    By addressing the identified issues and implementing these recommendations, Citi Bike can enhance its service quality and maintain its leadership in urban mobility solutions.

    Implementing these recommendations will require a focused effort on logistics, community engagement, and continuous monitoring of 
    usage data to ensure that the solutions align with user needs and urban dynamics.
    """)







