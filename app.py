from flask import Flask
from flask import render_template
import os

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
    return render_template("main.html")

if __name__ == "__main__":
    appEnv = "Cloud Foundry"
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
