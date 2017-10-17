import requests as rq
from datetime import datetime

import json
import shelve
import const

def get_utc_time(timestamp = None):
    if timestamp:
        d = datetime.fromtimestamp(timestamp)
        date = str(d.year) + str(d.month)+ str(d.day)
    else:
        now = datetime.utcnow()
        date = str(now.year) + str(now.month) + str(now.day)
    return date



def save_city_data():
    """This function will save the city data into shelve format
       This is an one time process. Can also be implemented to update the city list on a regular basis
    """
    with open(r"db\city_list.json",encoding = "utf-8") as data_file:
        cities =  json.load(data_file)
        #Creating cities database to retrive the id
        with shelve.open(r'db\cities') as db:
            for citi in cities:
                del citi['coord']
                key = citi['name']+citi['country']
                db[key] = citi
def store_city_temp_data(city_id):
    """This function will hit the api and store the data in local """
    url =  const.API_URL.format(city_id)
    response=rq.get(url)
    print(response.content)
    data=response.json()
    date = get_utc_time(data['dt'])
    text={'id': str(data['id']), 
                'name': data['name'], 
                'temp_min': data['main']['temp_min'], 
                'temp_max': data['main']['temp_max'], 
                'date': date}
    with shelve.open(r'db\temperature') as db:
        db[str(data['id'])] = {date:text}
    return text

 