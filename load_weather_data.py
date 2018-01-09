import pandas as pd

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

path =r'.\data\weather\weather_data.csv'
weather_df = pd.read_csv(path,
                         dtype=weather_dtypes,
                         na_values=['m', 'M'])

weather_df["Date"] = pd.to_datetime(weather_df["Date"])
print("Weather loaded")