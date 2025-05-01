import pandas as pd
weather = pd.read_csv('./data.csv')

# Display the first few rows of the dataset
print(weather.head())
# Display the columns of the dataset
print(weather.columns)
# Display the shape of the dataset
print(weather.shape)
# Display the summary statistics of the dataset
print(weather.describe())

columns_to_drop = [
    'Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID', 
    'Mean Max Temp Flag', 'Mean Min Temp Flag', 'Mean Temp Flag', 
    'Extr Max Temp Flag', 'Extr Min Temp Flag', 'Total Rain Flag',
    'Total Snow Flag', 'Total Precip Flag', 'Snow Grnd Last Day Flag',
    'Dir of Max Gust Flag', "Dir of Max Gust (10's deg)", 
    'Spd of Max Gust (km/h)', 'Spd of Max Gust Flag'
]
weather.drop(columns=columns_to_drop, inplace=True, errors='ignore') # Drop unnecessary columns

# Drop the first 5 rows of the dataset
weather = weather.iloc[5:]

#replace NaN value in Mean Max Temp, Mean Min Temp, Mean Temp, Extr Max Temp, Extr Min Temp with interpolated values
temp_columns = ['Mean Max Temp (°C)', 'Mean Min Temp (°C)', 'Mean Temp (°C)',
    'Extr Max Temp (°C)', 'Extr Min Temp (°C)']
weather[temp_columns] = weather[temp_columns].interpolate(method='linear')

#replace NaN value in Total Rain, Total Snow, Total Precip with 0
new_columns = ['Total Rain (mm)', 'Total Snow (cm)', 'Total Precip (mm)']
weather[new_columns] = weather[new_columns].fillna(0)

#replace NaN value in Snow Grnd Last Day with 0
if 'Snow Grnd Last Day (cm)' in weather.columns:
    weather.loc[:, 'Snow Grnd Last Day (cm)'] = weather['Snow Grnd Last Day (cm)'].fillna(0)

#replace NaN value in Dir of Max Gust with seasonal average
if 'Dir of Max Gust (°)' in weather.columns:
    weather.loc[:, 'Dir of Max Gust (°)'] = weather['Dir of Max Gust (°)'].fillna(weather['Dir of Max Gust (°)'].mean())
