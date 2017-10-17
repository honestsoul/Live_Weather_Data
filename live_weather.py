from flask import Flask, request, render_template, abort
from datetime import datetime
import requests
import shelve
API_URL = "http://api.openweathermap.org/data/2.5/weather?id={0}&appid=0218a2cb699302211c6d1248b1e83e67&units=Imperial"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html', text=request.form)

@app.route("/home", methods=['POST'])
def echo():
	text=request.form
	with shelve.open(r'db\cities') as db1:
		date=''.join(text.getlist('date')[0].split('-'))
		citi_id=text.getlist('city')[0] + text.getlist('country')[0]
		try:
			if citi_id in db1:
				city_id=db1[citi_id]['id']
				if city_id:
					def api_data():
						print(API_URL.format(city_id))
						response=requests.get(API_URL.format(city_id))
						print(response)
						data=response.json()
						text={'id': str(data['id']), 'name': data['name'], 'temp_min': data['main']
								['temp_min'], 'temp_max': data['main']['temp_max'], 'date': data['dt']}
						return text
					with shelve.open(r'db\temperature') as db:
						if str(city_id) in db:
							text_dict=db[str(city_id)]
							if date in text_dict:
								text = text_dict[date]
							else:
								text = api_data()
						else:
							text = api_data()		
			else:
				text={'output':"City data not found"}
		except KeyError :
			text={'error':'e'}
	return render_template('input.html', text = text)
if __name__ == '__main__':
   app.run()
