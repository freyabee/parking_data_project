from flask import Flask
from flask import render_template
import os

import pandas as pd
import numpy as np 
import folium as folium
from folium import plugins
from folium.plugins import HeatMap

def initmap():
    df = pd.read_csv('data/locations.csv', sep=',')
    df.head()

    df['Occupancy Percentage'] = pd.to_numeric(df['Occupancy Percentage'], errors='coerce')
    df['norm_occupancy'] = df['Occupancy Percentage'].apply(lambda x: x/100)
    df = df.dropna()
    
    unique = df['datetime'].unique()


    list_data = []
    for timestamp in unique:
        tempdf = df.loc[df['datetime']==timestamp]
        templist = [[row['latitude'],row['longitude'],row['norm_occupancy']] for index, row in tempdf.iterrows()]
        list_data.append(templist)

    parking = folium.Map(location=[50.7260218,-1.8827525], zoom_start = 13, tiles="OpenStreetMap")
    hm = plugins.HeatMapWithTime(list_data, index=[date for date in unique], auto_play=False,radius=40, max_opacity=0.8)
    hm.layer_name = 'Heatmap'
    parking.add_child(hm)

    minimap = plugins.MiniMap()
    parking.add_child(minimap)
    
    json14 =  os.path.join('data', 'carparkmap.json')    
    for property_name, property_value in features["json14"].items():
        
        print(property_name, property_value)



    #Load GeoJson

    folium.GeoJson(
        json14,
        name='geojson').add_to(parking)
    folium.LayerControl().add_to(parking)
    parking.save(outfile='templates/map.html')



initmap()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("map.html")

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
