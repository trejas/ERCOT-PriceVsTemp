import glob
import pandas as pd

# get data file names
path_2013 =r'.\data\day_ahead_pricing\2013'
filenames_2013 = glob.glob(path_2013 + "/*.csv")
path_2014 =r'.\data\day_ahead_pricing\2014'
filenames_2014 = glob.glob(path_2014 + "/*.csv")
path_2015 =r'.\data\day_ahead_pricing\2015'
filenames_2015 = glob.glob(path_2015 + "/*.csv")
path_2016 =r'.\data\day_ahead_pricing\2016'
filenames_2016 = glob.glob(path_2016 + "/*.csv")
path_2017 =r'.\data\day_ahead_pricing\2017'
filenames_2017 = glob.glob(path_2017 + "/*.csv")

dfs = []
for filename in filenames_2013:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
frame_2013 = pd.concat(dfs, ignore_index=True)

dfs = []
for filename in filenames_2014:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
frame_2014 = pd.concat(dfs, ignore_index=True)

dfs = []
for filename in filenames_2015:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
frame_2015 = pd.concat(dfs, ignore_index=True)

dfs = []
for filename in filenames_2016:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
frame_2016 = pd.concat(dfs, ignore_index=True)

dfs = []
for filename in filenames_2017:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
frame_2017 = pd.concat(dfs, ignore_index=True)

print("DA Prices Loaded")