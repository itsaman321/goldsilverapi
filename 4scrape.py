from bs4 import BeautifulSoup
import requests, re
import json



def Data():
	headers = { 
				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
			}
	
	r = requests.get(f'http://bcast.apjewellers.co.in:7767/VOTSBroadcastStreaming/Services/xml/GetLiveRateByTemplateID/apjewellers', headers = headers)
	soup = BeautifulSoup(r.content, 'lxml')
	d = soup.find('p').text.strip().split()

	d1 = {
	"PRODUCT":"SELL",
	"GOLD 99.5": d[-10]	,
	"GOLD 99.99":	d[-3]

	}
	d2 = {
	"GOLD":[d[2],d[3],d[4],d[5]],
	"SIVER":[d[8],d[9],d[10],d[11]],
	"INR":[d[14],d[15],d[16],d[17]]

	}
	d3 = {
	"GOLD":[d[20],d[21],d[22],d[23]],
	"SILVER COSTING":[d[27],d[28],d[29],d[30]]

	}
	data = [d1,d2,d3]


	return data


####################################################################################################################################################
from flask import Flask, jsonify, request

app = Flask(__name__)
#

# @app.route("/")
# def index():
#     return "<p>Hello, World!</p>"

@app.route("/rate", methods=['GET'])
def Rate():
	if request.method == 'GET':
		data = Data()
		return jsonify(data)



 

