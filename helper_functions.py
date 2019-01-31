import pandas as pd
import numpy as np 
import folium as folium
from folium import plugins
from folium.plugins import HeatMap
import os


def data_init():
	df = pd.read_csv('data/locations.csv', sep=',')
    df.head()

    df['Occupancy Percentage'] = pd.to_numeric(df['Occupancy Percentage'], errors='coerce')
    df['norm_occupancy'] = df['Occupancy Percentage'].apply(lambda x: x/100)
    df = df.dropna()
    
    unique = df['datetime'].unique()
	return unique, df

def return_list():
	list_data = []
	unique, df = data_init()
    for timestamp in unique:
        tempdf = df.loc[df['datetime']==timestamp]
        templist = [[row['latitude'],row['longitude'],row['norm_occupancy']] for index, row in tempdf.iterrows()]
        list_data.append(templist)
	return list_data