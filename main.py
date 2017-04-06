# my imports
from flask import Flask
#from datetime import datetime, timedelta

# GAE imports
from google.appengine.api import urlfetch

app = Flask(__name__)

@app.route('/')
def index():
	url = 'https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json?&start_date=2017-03-07&end_date=2017-04-06&column_index=4api_key=AFL4TBHtwc8xcD3ezLDy'
	response = urlfetch.fetch(url, validate_certificate=true)
	if responce.status_code == 200:
		return "<html><body> {} </body></html>".format( response.content )
	else:
		return "<html><body> {} </body></html>".format( "fuck")


