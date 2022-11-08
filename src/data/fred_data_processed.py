import os

import pandas as pd

data_dir = r'C:\Users\chris\Documents\Fall 2022\ECE 5424 - Advanced Machine Learning\Project\Project Files\ece_5424_project\data'

interim_dir = data_dir + r'\interim'
processed_dir = data_dir + r'\processed'

files = os.listdir(interim_dir)

for file in files:
    filename = file[:-8]
    interim_filepath = interim_dir + '\\' + filename + '.feather'
    processed_filepath = processed_dir + '\\' + filename + '.feather'
    if not os.path.exists(processed_filepath):
        df = pd.read_feather(interim_filepath)
        df = df.set_index('observation_date').resample('D').interpolate().reset_index()
        df.to_feather(processed_filepath)