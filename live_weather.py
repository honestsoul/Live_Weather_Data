from flask import Flask, request, render_template, abort
from datetime import datetime
import helper_util 
import requests
import shelve
import const

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html', text=request.form)

#ToDo - Need to work on this to implement more error codes
@app.errorhandler(401)
def custom_401(error):
    return {"Message":"Error"}

@app.route("/home", methods=['POST'])
def echo():
	text=request.form
	#The Shelve model is used for data store
	with shelve.open(r'db\cities') as db1:
		date=''.join(text.getlist('date')[0].split('-'))
		citi_id=text.getlist('city')[0] + text.getlist('country')[0]
		try:
			if citi_id in db1:
				city_id=db1[citi_id]['id']
				if city_id:
					with shelve.open(r'db\temperature') as db:
						if str(city_id) in db:
							text_dict=db[str(city_id)]
							if date in text_dict:
								text = text_dict[date]
							else:
								current_date = helper_util.get_utc_time()
								if date < current_date:
									text = {"message":"Historical data not availabe for the selected city"}
								elif date > current_date:
									text = {"message":"We don't provide forcast"}
								else:
									text = helper_util.store_city_temp_data(str(city_id))
						else:
							print(str(city_id))
							text = helper_util.store_city_temp_data(str(city_id))		
			else:
				text={'output':"City data not found"}
		except KeyError :
			text={'error':'e'}
	return render_template('input.html', text = text)
if __name__ == '__main__':
   app.run()
