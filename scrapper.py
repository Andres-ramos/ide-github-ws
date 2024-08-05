import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

url = "https://forecast.weather.gov/MapClick.php?lat=29.6742&lon=-82.3363&unit=0&lg=english&FcstType=digital"

html_string = requests.get(url).text


soup = BeautifulSoup(html_string)

data = soup.find_all("td", attrs={"color": "#FF0000"})

soup = BeautifulSoup(html_string,features='html.parser')

        #temperature
red_entries_list = soup.find_all("font", attrs={"color": "#FF0000"})
temperatures = [entry.text for entry in red_entries_list[1:25]]
print(temperatures)

dates = soup.find_all("table")
table = dates[4]
hours = []
for hour in table.find_all("td", attrs={"class": "date"})[25:49]:
    now = datetime.datetime.now()
    year = now.year
    day = now.day
    month = now.month
    dt_object = datetime.datetime(year, month, day, int(hour.text))
    hours.append(dt_object)

data = {"time": hours, "temperature": temperatures}
print(data)

df = pd.DataFrame(data)
print(df)