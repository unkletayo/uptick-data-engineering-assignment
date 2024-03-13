import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

current_directory = os.path.dirname(os.path.abspath(__file__))

print("Dataset downloaded in:", current_directory)

dataset_slug = 'nelgiriyewithana/indian-weather-repository-daily-snapshot'

api.dataset_download_files(dataset_slug, path=current_directory, unzip=True)

