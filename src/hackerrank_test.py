import requests
import re

def weatherStation(keyword=''):
    api_url = "https://jsonmock.hackerrank.com/api/weather/"
    if keyword != '':
        api_url = fr"https://jsonmock.hackerrank.com/api/weather/search?name={keyword}"

    result = requests.get(api_url)
    data = result.json()

    data_list = []
    for row in data['data']:
        weather_str = re.sub("\D", "", row['weather'])
        wind_str = re.sub("\D", "", row['status'][0])
        humidity_str = re.sub("\D", "", row['status'][1])
        csv_str = fr"{row['name']},{weather_str},{wind_str},{humidity_str}"
        data_list.append(csv_str)

    return(sorted(data_list))
  

# With search filter
print(weatherStation('Abu Dhabi'))

# With all data /Without filter
print(weatherStation())
