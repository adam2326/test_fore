# my imports
from flask import Flask
#from datetime import datetime, timedelta

# GAE imports
from google.appengine.api import urlfetch


app = Flask(__name__)


# define utility functions
def handle_stockdata_request(rpc, ticker):
	result = rpc.get_result()
	api_result = [ticker, result.content]


@app.route('/')
def index():
	tickers = ['GOOG','AAPL']
	urls = []
	rpcs = []
	for ticker in tickers:
		# build the url
		base_url = "https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".json?"
		start_date = "&start_date=" + start 
		end_date = "&end_date="+ end
		column_index = "&column_index=4"
		api_key = "api_key=AFL4TBHtwc8xcD3ezLDy"
		url = base_url + start_date + end_date + column_index + api_key
		urls.append(url)
	for url in urls:
	    rpc = urlfetch.create_rpc()
	    rpc.callback = functools.partial(handle_stockdata_request, rpc)
	    urlfetch.make_fetch_call(rpc, url)
	    rpcs.append(rpc)
	return "<html><body> {} <br><br><br><br><br><br><br><br> {} </body></html>".format( rpc[0], rpc[1] )
