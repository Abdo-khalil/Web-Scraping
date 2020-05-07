import requests
import urllib.request
from bs4 import BeautifulSoup 
import pandas as pd

# training scraping on forecast.weather  web site link >>>  <https://forecast.weather.gov/MapClick.php?lat=34.14575000000008&lon=-116.98306999999994#.XqGRWCPVLIU>

url = requests.get( "https://forecast.weather.gov/MapClick.php?lat=34.14575000000008&lon=-116.98306999999994#.XqGRWCPVLIU" )
soup = BeautifulSoup(url.content,"html.parser")
head = soup.find_all('li')
lis = soup.find_all(class_='tombstone-container')

# print(lis[0].find(class_='period-name').get_text())
# print(lis[0].find(class_ = 'short-desc').get_text())
# print(links[0].find(class_ = 'temp').get_text())

period_name = [l.find(class_='period-name').get_text()  for l in lis]
short_description = [l.find(class_='short-desc').get_text()  for l in lis]
tempreturre_high = [l.find(class_='temp').get_text() for l in lis]

weather_stuff = pd.DataFrame(
 	{
  		'period' : period_name,
		'description' : short_description,
		'tempreturre': tempreturre_high
 	})

print(weather_stuff)
weather_stuff.to_csv('weather.csv')