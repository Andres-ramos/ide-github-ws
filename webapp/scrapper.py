from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
from typing import Dict, List
from time import gmtime, strftime

class Scrapper:
    BASE_URI = "https://forecast.weather.gov/MapClick.php?lat=29.6742&lon=-82.3363&unit=0&lg=english&FcstType=digital"

    def fetch_data(self, latitude, longitude) -> Dict[str, List[str]]:
        """
        Fetches data from page.
        Output:
            {
                "date": [date],
                "temperatures": [temperature]
            }
        """
        #http request
        params = {
            "lat": latitude,
            "lon": longitude,
            "unit": 0,
            "lg": "english",
            "FcstType": "digital"
        }
        response = requests.get(self.BASE_URI, params=params)

        html_string = response.text
        soup = BeautifulSoup(html_string,features='html.parser')

        #temperature
        red_entries_list = soup.find_all("font", attrs={"color": "#FF0000"})
        temperatures = [entry.text for entry in red_entries_list[1:25]]

        #date
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

        return {"time": hours, "temperature": temperatures}