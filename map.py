"""
This program open a map using foluim library
"""
import folium

m = folium.Map(location = [41.015137, 28.979530])
m.save("istanbul_map.html")
