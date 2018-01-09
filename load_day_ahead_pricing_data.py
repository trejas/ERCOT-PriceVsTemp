'''
    Author: Traey Hatch
    This file loads data from a local CSV file for use
    in a data analysis and predictive experiment.

    All years are loaded to a single dataframe.

'''
import glob
import pandas as pd


def get_data_filenames(years):
    # get the file names from several csv files stored in
    # a folder structure.
    filenames = []

    # Add filenames to a list
    for year in years:
        path = r'.\data\day_ahead_pricing\{}'.format(year)
        filenames.extend(glob.glob(path + "/*.csv"))

    return filenames


def load_data(years):
    # Load data from .csv files into a Pandas DataFrame
    dfs = []

    # Get filenames to aggregate
    filenames = get_data_filenames(years)

    # Aggregate file contents to single dataframe
    for filename in filenames:
        dfs.append(pd.read_csv(filename))

    # Concatenate all data into one DataFrame
    day_ahead_pricing_df = pd.concat(dfs, ignore_index=True)

    print("Day Ahead Prices Loaded")

    return day_ahead_pricing_df


day_ahead_pricing_df = load_data([2013, 2014, 2015, 2016, 2017])
