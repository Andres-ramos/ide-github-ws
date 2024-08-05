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

        """
        return 