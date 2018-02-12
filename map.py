
"""
This program open a map using foluim library
"""

import folium
import webbrowser
import os
import pandas as pd


m = folium.Map(location = [41.015137, 28.979530])
folium.Marker(location = [41.015137, 28.979530]).add_to(m)
m.save("istanbul_map.html")
path = os.path.abspath("istanbul_map.html")
url = "file://" + path
webbrowser.open(url)
