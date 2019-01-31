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


#@app.route("/")
#def index():
    #return render_template("map.html")
	
@app.route('/')
def asset_data():
    url = 'https://gateway.eu1.mindsphere.io/api/assetmanagement/v3/assets/{0}/aspects'.format("2780aabba30d4b1083c284adb80b1f09")
    try:
        response = requests.get(url, headers=requestHeaders())
        if not response.status_code == 200:
            eprintMS(getframeinfo(currentframe()), response.content)
            return render_template('index.html', assets_data = None, error = "MindSphere API Error / Failed to get assets")
        data = json.loads(response.text)
        print(json.dumps(data, indent = 4))
        return render_template('index.html', assets_data = data, error = None)
    except requests.ConnectionError:
        eprintMS(getframeinfo(currentframe()), "MindSphere failed to connect to itself")
        return render_template('index.html', assets_data = data, error = "MindSphere failed to connect to itself")

# Prints detailed error messages
def eprintMS(frameinfo, message):
    print(frameinfo.filename, ":", frameinfo.lineno, "/", message)

def requestHeaders():
    headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleS1pZC0xIiwidHlwIjoiSldUIn0.eyJqdGkiOiI2Zjc3ZDQ2NzhiZjI0Y2IzOGE0MDdkNWU2NWJkYmY1YSIsInN1YiI6ImQxYTkwZjVjLWVhMzQtNGQ5Yi04NGY3LTc3MmJmZWVlZmNiOSIsInNjb3BlIjpbIm1kc3A6Y29yZTppb3QuYnVsa1RpbVVzZXIiLCJ0b210b2tlbmFwcC5hbGwiLCJtZHNwOmNvcmU6aW90LmJ1bGtUaW1BZG1pbiIsInVhYS5vZmZsaW5lX3Rva2VuIiwibWRzcDpjb3JlOmFzc2V0bWFuYWdlbWVudC5zdGFuZGFyZHVzZXIiXSwiY2xpZW50X2lkIjoidG9tdG9rZW5hcHAtbWluZWRldiIsImNpZCI6InRvbXRva2VuYXBwLW1pbmVkZXYiLCJhenAiOiJ0b210b2tlbmFwcC1taW5lZGV2IiwiZ3JhbnRfdHlwZSI6ImF1dGhvcml6YXRpb25fY29kZSIsInVzZXJfaWQiOiJkMWE5MGY1Yy1lYTM0LTRkOWItODRmNy03NzJiZmVlZWZjYjkiLCJvcmlnaW4iOiJtaW5lZGV2IiwidXNlcl9uYW1lIjoidmlsbW9zLmFsdGJhY2tlckBzaWVtZW5zLmNvbSIsImVtYWlsIjoidmlsbW9zLmFsdGJhY2tlckBzaWVtZW5zLmNvbSIsImF1dGhfdGltZSI6MTU0ODk1MjQ3MywicmV2X3NpZyI6IjU1M2UzYWYyIiwiaWF0IjoxNTQ4OTU0NjgwLCJleHAiOjE1NDg5NTY0ODAsImlzcyI6Imh0dHBzOi8vbWluZWRldi5waWFtLmV1MS5taW5kc3BoZXJlLmlvL29hdXRoL3Rva2VuIiwiemlkIjoibWluZWRldiIsImF1ZCI6WyJtZHNwOmNvcmU6aW90IiwidG9tdG9rZW5hcHAtbWluZWRldiIsInVhYSIsIm1kc3A6Y29yZTphc3NldG1hbmFnZW1lbnQiLCJ0b210b2tlbmFwcCJdLCJ0ZW4iOiJtaW5lZGV2Iiwic2NoZW1hcyI6WyJ1cm46c2llbWVuczptaW5kc3BoZXJlOmlhbTp2MSJdLCJjYXQiOiJ1c2VyLXRva2VuOnYxIn0.i1s2rjWhPvulQHxNWbTFfrf7twUxAsS8-L-e1mNpRePHdStDDVD4ncS0w7WfMJNjNi4YsdRVGAngPd6ViSqGnpe-8ZLO0m7rz6oxvWem99mkfc583NoHQVpJ9_XYr2uZRCkli7umwsKzRT7hWAzB0JauKPnYQYo5VR1R1c0k-g1Cfu3E2x_JbgPhxob7TfuB42jZzrQSXHZNSncGjY84mbmUm5FuBgG_KBcYhKKsZ-8A_Zo9FARmeaqogkQKBLMfUX3iyY1h6TXKgs16mBjhK8EFQvbOzHA1ji9758Yj1Z5Em2RdZSQbUPTqLHw-vuZxrRAqYtU1-pcIF3t-JEVNwQ'}
    return headers

if __name__ == "__main__":
    appEnv = "Cloud Foundry"
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
