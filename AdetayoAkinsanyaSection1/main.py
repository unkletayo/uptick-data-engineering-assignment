import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Get Absolute Current directory of this file
current_directory = os.path.dirname(os.path.abspath(__file__))

dataset_slug = 'nelgiriyewithana/indian-weather-repository-daily-snapshot'
api.dataset_download_files(dataset_slug, path=current_directory, unzip=True)

# I did this because the system is always tryint to read from the root folder containing the two assignments
# not where the python file was located
file_name="IndianWeatherRepository.csv"
csv_file_path = os.path.join(current_directory, file_name)

# Reading the weather data
weather_data = pd.read_csv(csv_file_path)
weather_data.dropna(inplace=True)  

# Generate summary statistics and insights from the data
summary_statistics = {
    'Mean Temperature': weather_data['temperature_celsius'].mean(),
    'Mean Precipitation': weather_data['precip_mm'].mean(),
    'Mean Temperature': weather_data['humidity'].mean(),
    'Standard Deviation Temperature': weather_data['temperature_celsius'].std(),
    'Standard Deviation Precipitation': weather_data['precip_mm'].std(),
    'Standard Deviation Humidity': weather_data['humidity'].std()
}



# Print the summary statistics
for key, value in summary_statistics.items():
    print(f"{key}: {value}")


# SECTION 2

# Group data by city
city_data = weather_data.groupby('location_name')

# Function to plot temperature and precipitation for a city
def plot_city_weather(city):
  city_weather = city_data.get_group(city)
  plt.figure(figsize=(10, 6))  

  # Extract temperature (assuming temperature_celsius is missing)
  try:
      temperature_column = 'temperature_celsius'
      temperature = city_weather[temperature_column]
  except KeyError:
      print(f"Warning: Temperature column '{temperature_column}' not found for city {city}")
      return

  # Extract precipitation (assuming precip_mm is missing)
  try:
      precipitation_column = 'precip_mm'
      precipitation = city_weather[precipitation_column]
  except KeyError:
      print(f"Warning: Precipitation column '{precipitation_column}' not found for city {city}")
      return

  # Plot temperature
  plt.plot(city_weather['last_updated'], temperature, label='Temperature (°C)')

  # Plot precipitation (secondary y-axis)
  ax2 = plt.twinx()
  ax2.plot(city_weather['last_updated'], precipitation, label='Precipitation (mm)', color='blue')
  ax2.set_ylabel('Precipitation (mm)')

  # Customize plot
  plt.title(f"Weather in {city}")
  plt.xlabel('Date')
  plt.ylabel('Temperature (°C)')
  plt.legend()
  plt.grid(True)
  plt.xticks(rotation=45)  # Rotate x-axis labels for readability
  plt.tight_layout()
  plt.show()

# Loop through each city and plot data


for city in city_data.groups:
  plot_city_weather(city)

# Get the first 3 cities
# first_three_cities = weather_data['location_name'].unique()[:3]

# Loop through the first 3 cities and plot data
# for city in first_three_cities:
#   plot_city_weather(city)
