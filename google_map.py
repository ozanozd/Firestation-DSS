"""
This progmram shows a istanbul using google static map API
"""
###################################################################################
# Works to do :
######## i)  If we decide to use google_maps api keep it
######## ii) Add necessary changes to see distircts

import gmplot

latitudes = [ 65.32 , 64.31]
longitudes = [ 26.15 , 27.63]
gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")
