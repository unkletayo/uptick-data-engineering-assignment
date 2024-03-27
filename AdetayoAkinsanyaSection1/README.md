**Setup Instructions for Running the Weather Analysis Code**

This Python script is designed to analyze and visualize weather data from the "Indian Weather Repository Daily Snapshot" dataset available on Kaggle. Before running the script, please follow these setup instructions:

**1. Install Required Packages:**

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Install the required Python packages by running the following command in your terminal or command prompt:
  ```
  pip3 install pandas matplotlib kaggle
  ```

**2. Kaggle API Authentication:**

- In order to download the dataset using the Kaggle API, you need to have a Kaggle account and obtain an API key.
- Go to the Kaggle website, log in or sign up for an account, and navigate to the 'Account' tab of your user profile.
- Scroll down to the 'API' section and click on 'Create New API Token'. This action will download a file named `kaggle.json`.
- Place the downloaded `kaggle.json` file in your home directory under `.kaggle` folder. If the `.kaggle` folder does not exist, create it manually.

**3. Dataset Download:**

- The script automatically downloads the dataset using the Kaggle API. You don't need to manually download the dataset.
- Ensure that you have enabled the Kaggle API on your account
- Update the `dataset_slug` variable in the script if necessary, depending on any changes to the dataset's location or name.

**4. Run the Script:**

- Once you have completed the above steps, navigate to the directory containing the Python script using the terminal or command prompt.
- Execute the script by running the following command:
  ```
  python3 main.py
  ```

**5. View Results:**

- After running the script, it will generate summary statistics and plots for temperature and precipitation data for each city included in the dataset.
- Summary statistics will be printed to the console.
- Plots for temperature and precipitation will be displayed on the screen for each city.

**Note:** Ensure that you have a stable internet connection while running the script, as it requires downloading the dataset from Kaggle. Additionally, make sure you have sufficient disk space available for storing the dataset.

Additional Notes:

- The script assumes the CSV file is named "IndianWeatherRepository.csv". If the downloaded file has a different name, modify the script (file_name variable) accordingly.
  The script currently loops through all cities in the dataset. You can uncomment the section that retrieves only the first three cities for a quicker test run.
- Ensure that you have a stable internet connection while running the script, as it requires downloading the dataset from Kaggle. Additionally, make sure you have sufficient disk space available for storing the dataset.
