from flask import Flask
from flask import render_template
import os
import requests
from inspect import currentframe, getframeinfo
import json

import pandas as pd
import numpy as np 
import folium as folium
from folium import plugins
from folium.plugins import HeatMap
from render_map import initmap



app = Flask(__name__)
#initmap()


@app.route("/")
def index():
    return render_template("map.html")
	
@app.route('/')
def asset_data():
    url = 'https://gateway.eu1.mindsphere.io/api/assetmanagement/v3/assets/{0}/aspects/'.format("2780aabba30d4b1083c284adb80b1f09")
    try:
        response = requests.get(url + "2780aabba30d4b1083c284adb80b1f09", headers=requestHeaders())
        if not response.status_code == 200:
            eprintMS(getframeinfo(currentframe()), response.content)
            return render_template('index.html', assets_data = None, error = "MindSphere API Error / Failed to get assets")
        data = json.loads(response.text)
        return render_template('index.html', assets_data = data, error = None)
    except requests.ConnectionError:
        eprintMS(getframeinfo(currentframe()), "MindSphere failed to connect to itself")
        return render_template('index.html', assets_data = data, error = "MindSphere failed to connect to itself")

# Prints detailed error messages
def eprintMS(frameinfo, message):
    print(frameinfo.filename, ":", frameinfo.lineno, "/", message)

def requestHeaders():
    try:
        int(os.getenv("VCAP_APP_PORT"))!= 5000 #app is running in cloud foundry
        headers =  {'Authorization': request.headers["Authorization"]}
    except:
        headers = {'Authorization': 'Bearer ' + token['access_token']}
    return headers

if __name__ == "__main__":
    appEnv = "Cloud Foundry"
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
