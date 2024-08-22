# CitiBike-New York Analysis Project

## Project Overview
This project leverages Python and Streamlit to analyze CitiBike usage in New York City, aiming to enhance operational efficiency and improve customer engagement. By identifying high-demand areas, suggesting optimal locations for new stations, and exploring the impacts of weather conditions on bike usage, this project provides actionable insights to stakeholders.

## Features

- **Virtual Environment Setup**: Ensures isolated Python environments for reliable dependency management.
- **Data Integration**: Combines historical trip data from 12 monthly datasets of 2022 from NOAA with weather data and a dataset from CitiBike, using Python pandas to assess influences on bike usage patterns.
- **Interactive Dashboard**: Utilizes Streamlit to visualize data interactively, showcasing usage statistics, popular routes, and station distribution in a user-friendly web application.
- **Predictive Insights**: Employs machine learning models to predict station placement and bike availability, optimizing resource allocation.
- **Dual-Axis Plotting**: Implements dual-axis time series plotting with Plotly to visualize the relationship between weather conditions and bike usage.
- **Kepler.gl Visualization**: Uses Kepler.gl for dynamic mapping, visualizing trip data effectively, and analyzing trip frequencies and patterns.

## Project Implementation Details

### Data Sources
The data used in this project is sourced from open datasets provided by Citi Bike and NOAA for the year 2022:
- Citi Bike Data: [Citi Bike Trip Data](https://s3.amazonaws.com/tripdata/index.html)
- NOAA Weather Data: [NOAA Climate Data Online](https://www.noaa.gov/)

Due to the extensive size of the datasets (12 individual monthly datasets from NOAA and a dataset from Citi Bike), the main DataFrame was too large to be uploaded directly to GitHub. The data integration and manipulation were performed using Python's pandas library to ensure comprehensive analysis and insights.

### Data Analysis Techniques
- **Data Preparation**: Combines and cleanses bike usage and weather data to analyze how varying weather conditions affect bike usage trends.
- **Predictive Analytics**: Utilizes forecasting techniques to predict demand and optimize bike distribution across various stations.

### Kepler.gl Configuration
- **Map Customization**: Configures Kepler.gl to visualize trip data effectively, using customized point colors and adding arcs to represent frequent routes.
- **Dynamic Filtering**: Implements interactive filters to focus on the most common trips and analyze busy zones, aiding in strategic planning for new station locations.

  ### Deployment
**Streamlit App** The Dashboard was deployed. [View Dashboard on Streamlit](https://citibike-new-york-2.streamlit.app/)

## Getting Started

### Prerequisites
Ensure your machine has Python installed along with the following libraries:
- `Pandas`
- `Numpy`
- `Matplotlib`: Essential for creating static and interactive visualizations.
- `Requests`: For handling HTTP requests to fetch data.
- `Seaborn`: Advanced visualization.
- `Kepler.gl`: For geospatial data visualization.
- `Streamlit`: For deploying interactive and live data applications.

### Installation
Clone the repository to get started with the project:
```bash
git clone https://github.com/YourUsername/CitiBike-New-York.git
