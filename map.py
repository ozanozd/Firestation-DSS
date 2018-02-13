
"""
This program open a map using foluim library
"""

import folium
import webbrowser
import os
import pandas as pd
import re
import gmplot

lan = 28.241 , 28.214 , 28.351
lon = 41.01 , 41.0124 , 41.5325
points = []
points1 = []
lats = []
lats1 = []
longs = []
longs1 = []
file = open('polygon.txt' , 'r')
for line in file :
    line = line.strip()
    s = re.split(r'\t+', line)
    points.append(s)

for element in points:
    element[0] = float(element[0])
    element[1] = float(element[1])

for element in points :
    lats.append(element[0])
    longs.append(element[1])

file.close()

file1 = open('polygon1.txt' , 'r')
for line in file1 :
    line = line.strip()
    s = re.split(r'\t+', line)
    points1.append(s)

for element in points1:
    element[0] = float(element[0])
    element[1] = float(element[1])

for element in points1 :
    lats1.append(element[0])
    longs1.append(element[1])

#file = open('last.txt' ,  'w')

gmap = gmplot.GoogleMapPlotter(longs[0] , lats[0]   ,   10)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap.polygon(longs , lats , color = 'green' , c = 'red' , title  = 'Kadikoy')
gmap.polygon(longs1 , lats1 , color = 'green' , c = 'red' , title = 'Umraniye')
gmap.marker(lat = 41.0265124 , lng = 29.1559124  , color = 'red' , title = 'Umraniye Dudullu Risk A')

gmap.draw("last_map.html")
path = os.path.abspath("last_map.html")
url = "file://" + path
webbrowser.open(url)

"""
m = folium.Map(location = [41.015137, 28.979530])
folium.Plot(locations = points , color = 'yellow' , opacity = 1).add_to(m)
m.save("istanbul_map.html")
path = os.path.abspath("istanbul_map.html")
url = "file://" + path
webbrowser.open(url)
"""
