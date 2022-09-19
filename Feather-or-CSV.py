# %% Importing the libraries

import pandas as pd
import numpy as np
import time
import os

# %% Simulating data

columns = 5
rows = 1_000_000

np.random.seed(0)
df = pd.DataFrame(np.random.rand(rows, columns),
                  columns=["c1", "c2", "c3", "c4", "c5"])

# %% Using Feather

tic = time.process_time()
df.to_feather('data.feather')
feather_write = time.process_time() - tic
tic = time.process_time()
feather = pd.read_feather('data.feather')
feather_read = time.process_time() - tic

# %% Using .csv

tic = time.process_time()
df.to_csv('data.csv', index=False)
csv_write = time.process_time() - tic
tic = time.process_time()
csv = pd.read_csv('data.csv')
csv_read = time.process_time() - tic

#%% Computing the file size

def get_file_size_in_megabytes(file_name, decimals=2):
    file_stats = os.stat(file_name)
    return round(file_stats.st_size / (1024 * 1024), decimals)

feather_file_size = get_file_size_in_megabytes('data.feather')
csv_file_size = get_file_size_in_megabytes('data.csv')

#%% Comparing the times
# Comparing times
times = pd.DataFrame({'Write (s)': [feather_write, csv_write],
                      'Read (s)': [feather_read, csv_read],
                     'Size (mb)': [feather_file_size, csv_file_size]
                     },
                     index=['Feather', 'CSV'])
times
