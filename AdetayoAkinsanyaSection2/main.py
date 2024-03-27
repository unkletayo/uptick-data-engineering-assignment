import sqlite3
import csv


# Connect to SQLite database
connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()




create_table_query="""
CREATE TABLE IF NOT EXISTS weather(
      country TEXT,
    location_name TEXT,
    region TEXT,
    latitude REAL,
    longitude REAL,
    timezone TEXT,
    last_updated_epoch INTEGER,
    last_updated TEXT,
    temperature_celsius REAL,
    temperature_fahrenheit REAL,
    condition_text TEXT,
    wind_mph REAL,
    wind_kph REAL,
    wind_degree INTEGER,
    wind_direction TEXT,
    pressure_mb REAL,
    pressure_in REAL,
    precip_mm REAL,
    precip_in REAL,
    humidity INTEGER,
    cloud INTEGER,
    feels_like_celsius REAL,
    feels_like_fahrenheit REAL,
    visibility_km REAL,
    visibility_miles REAL,
    uv_index REAL,
    gust_mph REAL,
    gust_kph REAL,
    air_quality_Carbon_Monoxide REAL,
    air_quality_Ozone REAL,
    air_quality_Nitrogen_dioxide REAL,
    air_quality_Sulphur_dioxide REAL,
    air_quality_PM2_5 REAL,
    air_quality_PM10 REAL,
    air_quality_us_epa_index REAL,
    air_quality_gb_defra_index REAL,
    sunrise TEXT,
    sunset TEXT,
    moonrise TEXT,
    moonset TEXT,
    moon_phase TEXT,
    moon_illumination INTEGER
)
"""

cursor.execute(create_table_query)

print(connection.total_changes)


with open('../AdetayoAkinsanyaSection1/IndianWeatherRepository.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        values = [row[key] for key in row.keys()]
        cursor.execute("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

# Commit changes and close connection


connection.commit()
# connection.close()



# Fetch and print first few rows
# rows = cursor.execute("SELECT * FROM weather LIMIT 5").fetchall()
# for row in rows:
#     print(row)
  
# Close connection
connection.close()
