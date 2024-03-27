## Setting Up a SQLite Database for Weather Data (Markdown)

This script demonstrates how to import weather data from a CSV file into a SQLite database. Here's a breakdown of the steps involved:

**1. Importing Libraries:**

- `sqlite3`: This built-in Python library allows interaction with SQLite databases.
- `csv`: This library helps read and write data in CSV format.

**2. Connecting to the Database:**

- The script establishes a connection to a database named `weather_data.db` using `sqlite3.connect`.
- A cursor object is created using `connection.cursor()` to execute SQL statements.

**3. Creating the Database Table (if it doesn't exist):**

- The script defines a SQL query (`create_table_query`) to create a table named `weather` with various weather data columns like `country`, `location_name`, `temperature_celsius`, etc.
- `cursor.execute` executes the query, creating the table if it doesn't already exist (`IF NOT EXISTS` clause).
- `connection.total_changes` displays the number of rows affected by the table creation (usually 0 if the table already existed).

**4. Importing Data from CSV:**

- The script opens the CSV file named `IndianWeatherRepository.csv` located in a sibling directory (`../AdetayoAkinsanyaSection1/`).
- `csv.DictReader` reads the CSV file, treating each row as a dictionary where column names are keys and values are data points.
- The script iterates through each row (`for row in csv_reader`) and extracts the values using a list comprehension (`[row[key] for key in row.keys()]`).
- An `INSERT INTO` SQL statement is executed for each row, inserting the extracted values into the corresponding columns of the `weather` table.

**5. Committing Changes and Closing Connection:**

- `connection.commit()` saves the changes made to the database.
- Finally, `connection.close()` releases the connection to the database, ensuring proper resource management.

**Note:** The commented-out section demonstrates how to fetch and print the first few rows of data from the table using `cursor.execute` and `fetchall`.

**Additional Notes:**

- Make sure you have the `sqlite3` library installed (`pip install sqlite3`).
- Adjust the CSV file path (`'../AdetayoAkinsanyaSection1/IndianWeatherRepository.csv'`) if your file location differs.
- This script assumes the CSV file has the same structure (column names) as the weather data.
