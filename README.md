The given portal(openweathermap.org) provides only 60 calls per minutes in free subscription. 
It means it will take more than 24 hours to fetch the temperature for all the available cities.
In order to make this code simple and scalable, the daily job only sync the Austin data.
For other cities, it fetches the data by calling the API directly.
The daily job can be scaled to sync daily weather data for all the cities.


Technology -  Python 3.5.6
Framework  -  Flask
Database   -  Python's Shelves DB
HTML5, Bootstrap 3.x ,Jinja2


Note : 

As I was not able to work on the below due to office work but below are the area of improvement - 

1. Improve to scale in a distributed fashion.
2. Modularize the code further.
3. Create an Standard and Secure DB .
4. Improve the batch job in scheduler.py
5. Create an Eye catching UI template
6. Handle more error messages
7. Improve the test case coverage
8. Create the micro services


