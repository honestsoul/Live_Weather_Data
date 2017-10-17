import schedule
import time
import const
import helper_util


'''
Please Read 

If we need to store the data for all the cities, we need to run this in concurrent mode.abs
Since the Free subcription of openweathermap.org gives only 60 API calls per minute, 
it is not feasible to get the data for all the cities.
'''

def job():
    #Currently working for only one city ie. Austin
    #As cities have limited access for API in free version, we may want to implement some kind for message broker such as celery for scaling
    for city in const.CITY_ID_LIST:
        helper_util.store_city_temp_data(city)

#Scheduling the Job at the starting and End of the day
schedule.every().day.at("00:01").do(job)
schedule.every().day.at("23:50").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)