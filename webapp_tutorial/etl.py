from webapp.scrapper import Scrapper
from webapp.app import create_app
from webapp.db import get_db
# from webapp.model import Temperature
# from app import db

app = create_app()

def run_etl():
    #Extract 
    # lat = 18.403958942814228
    # lon = -66.04510186605337
    # c = Scrapper()
    # data = c.fetch_data(lat, lon)
    
    # #Transform
    # temps = data["temperature"]
    # dates = data["time"]

    # #load
    # with app.app_context():
    #     db = get_db()
    #     for temp, date in zip(temps, dates):
    #         db.execute(
    #             'INSERT INTO temperature (lat, lon, temperature, time)'
    #             ' VALUES (?, ?, ?, ?)',
    #             (lat, lon, temp, date)
    #         )
    #     db.commit()
    # return 
    return 
run_etl()