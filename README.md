# CitiBike-New York Analysis Project

## Project Overview
This project analyzes CitiBike usage in New York to identify patterns and provide insights into the operational efficiency and customer engagement of the bike-sharing system. The analysis aims to pinpoint high-demand areas, suggest optimal locations for new bike stations, and explore the impact of weather conditions on bike usage.

## Features

- **Data Integration**: Combines historical trip data with weather data to assess influences on bike usage patterns.
- **Interactive Dashboard**: Visualizes data through an interactive dashboard that displays usage statistics, popular routes, and station distribution.
- **Predictive Insights**: Offers predictive insights for station placement and bike availability to optimize resource allocation.
- **Dual-Axis Plotting**: Utilizes dual-axis time series plotting to visualize the relationship between weather conditions (temperature) and bike usage patterns, highlighting how external factors influence customer behavior.
- **Kepler.gl Visualization**: Incorporates Kepler.gl to map trip data dynamically, allowing for the visualization of popular routes and the analysis of trip frequencies and patterns.

## Project Implementation Details

### Kepler.gl Configuration
- **Map Customization**: Configured Kepler.gl to visualize trip data, adjusting point colors and adding arcs to represent routes effectively.
- **Filtering Data**: Applied filters to identify and visualize the most common trips, such as those between Hoboken Terminal and Monmouth St, and trips around the South Waterfront Walkway.
- **Data Insights**: Analyzed the busy zones and the impact of location on trip frequency, contributing to strategic planning for new bike stations.

### Data Analysis Techniques
- Combined and cleaned bike usage and weather data to understand how different weather conditions affect bike usage trends.
- Implemented predictive analytics for forecasting demand and optimizing the distribution of bikes across stations.

## Getting Started

### Prerequisites
Ensure you have Python installed on your machine along with the following libraries:
- Pandas
- Numpy
- Matplotlib: Used extensively for generating static, interactive, and animated visualizations.
- Requests
- Seaborn
- Kepler.gl for Python: For mapping and visualization tasks.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/CitiBike-New-York.git
