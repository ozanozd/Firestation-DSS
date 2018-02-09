"""
This program open a map using foluim library
"""
import folium
import webbrowser
import os
import pandas as pd

state_geo = os.path.join('data' , 'cities_of_turkey.json')
m = folium.Map(location = [41.015137, 28.979530])
folium.GeoJson(
    state_geo ,
    name = 'geojson'
).add_to(m)
m.save("istanbul_map.html")
path = os.path.abspath("istanbul_map.html")
url = "file://" + path
webbrowser.open(url)
