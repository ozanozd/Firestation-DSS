
"""
This program open a map using foluim library
"""

#General library imports
import webbrowser
import os
import pandas as pd
import re
import gmplot

#Inside project imports
import read_file as reader

#Create the map as a global variable
gmap = gmplot.GoogleMapPlotter(41.015137, 28.979530 , 10)

def add_marker(x_coordinates , y_coordinates , name_of_districts , solution_array):
    """
    This function add markers to some districts which indicates we will open a fire station in this particular district.
    It takes 4 arguments:
    i)   x_coordinates     : A list , whose length is NUMBER_OF_DISTRICT contains x coordinates of districts
    ii)  y_coordinates     : A list , whose length is NUMBER_OF_DISTRICT contains y coordinates of districts
    iii) name_of_districts : A list , whose length is NUMBER_OF_DISTRICT contains name of districts
    iv)  solution_array    : A list , whose length is NUMBER_OF_DISTRICT it contains binary values if ith element of it is 1 then we will open a fire station at ith district
    It returns nothing
    """
    for i in range(reader.util.NUMBER_OF_DISTRICT):
        #If the ith distict has a fire station add marker to it
        if solution_array[i] == 1:
            gmap.marker(lat = y_coordinates[i] , lng = x_coordinates[i] , color = 'red' , title = name_of_districts[i])

def run():
    """
    This function runs the map and show the correspding html
    """
    name_of_districts , x_coordinates , y_coordinates , from_district , to_district , distance = reader.read_district_file()
    solution_array = reader.read_binary_txt("solution.txt")
    add_marker(x_coordinates , y_coordinates , name_of_districts , solution_array)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    lats , longs = reader.polygon_coords("temp-nodes.xlsx")
    for i in range(975):
        gmap.polygon(longs[i] , lats[i] , color = 'green' , c = 'red')
    gmap.draw("last_map.html")
    path = os.path.abspath("last_map.html")
    url = "file://" + path
    webbrowser.open(url)

#run()
