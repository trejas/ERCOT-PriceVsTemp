'''
    Author: Traey Hatch
    This file loads data from a local CSV file for use
    in a data analysis and predictive experiment.

    All years are loaded to a single dataframe.

'''
import pandas as pd


def load_data():
    # Implicitly type the DataFrame column datatypes
    weather_dtypes = {
        'Date': 'str',
        'Time': 'object',
        'Temp': 'float',
        'RH': 'float',
        'Dewpt': 'float',
        'WindSpd': 'float',
        'WindDirection': 'float',
        'PeakWindGust': 'float',
        'LowCloudHt': 'float',
        'MedCloudHt': 'float',
        'HighCloudHt': 'float',
        'Visibility': 'float',
        'AtmPress': 'float',
        'SeaLevPress': 'float',
        'Altimeter': 'float',
        'Precipip': 'float',
        'WindChill': 'object',
        'HeatIndex': 'object'
    }

    path = r'.\data\weather\weather_data.csv'
    weather_df = pd.read_csv(path,
                             dtype=weather_dtypes,
                             na_values=['m', 'M'])

    weather_df["Date"] = pd.to_datetime(weather_df["Date"])
    print("Weather loaded")

    return weather_df


weather_df = load_data()
