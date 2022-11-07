import os

import pandas as pd

data_dir = r'C:\Users\chris\Documents\Fall 2022\ECE 5424 - Advanced Machine Learning\Project\Project Files\ece_5424_project\data'

raw_dir = data_dir + r'\raw'
interim_dir = data_dir + r'\interim'

files = os.listdir(raw_dir)

for file in files:
    filename = file[:-4]
    raw_filepath = raw_dir + '\\' + file
    interim_filepath = interim_dir + '\\' + filename + '.feather'
    if not os.path.exists(interim_filepath):
        df = pd.read_excel(raw_filepath, skiprows=10, parse_dates=True)
        df.to_feather(interim_filepath)
