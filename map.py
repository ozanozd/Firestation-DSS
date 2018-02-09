import folium
import webbrowser

m = folium.Map(location = [ 41.213 , 28.1241])
folium.Marker(location = [41.213 , 28.1241]).add_to(m)
m.save("istanbul.html")
webbrowser.open("istanbul.html")
