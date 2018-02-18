
"""
This program open a map using foluim library
"""

import folium
import webbrowser
import os
import pandas as pd
import re
import gmplot
import read_excel_trial as helper

#Define number of districts as a constant
NUMBER_OF_DISTRICTS = 867

#Create the map as a global variable
gmap = gmplot.GoogleMapPlotter(41.015137, 28.979530 ,   10)

def add_marker(x_coordinates , y_coordinates , name_of_districts , binary_array):
    """
    This function takes 3 arguments:
    i)   x_coordinates : A list of x coordinates with lenght NUMBER_OF_DISTRICT
    ii)  y_coordinates : A list of y coordinates with lenght NUMBER_OF_DISTRICT
    iii) name_of_districts : A list of district name with lenght NUMBER_OF_DISTRICT
    iv)  binary_array : A list of binary values , if ith element of it is 1 then we will open a fire station at ith district

    Then this function add markers to map with appropriate coordinates with hooker.
    """
    for i in range(NUMBER_OF_DISTRICTS):
        #If the ith distict has a fire station add marker to it
        if binary_array[i] == 1:
            gmap.marker(lat = y_coordinates[i] , lng = x_coordinates[i] , color = 'red' , title = name_of_districts[i])

def prepare_points(filename):
    """
    This function takes filename of the solution and creates x_coordinates , y_coordinates , name_of_districts , binary_array
    """

    fire_station_points = []
    binary_array = helper.read_binary_txt(filename)
    x_coordinates , y_coordinates = helper.get_x_y_coordinates('MahalleVerileri.xlsx')
    name_of_districts = helper.get_district_names('MahalleVerileri.xlsx')
    return x_coordinates , y_coordinates , name_of_districts , binary_array

def read_polygon(filename):
    """
    This function takes one argument , filename , reads it and returns the corresponding polygon coordinates as lat,long
    """

    #Prepare lists
    points = []
    lats = []
    longs = []

    file = open(filename , 'r')
    for line in file :
        line = line.strip()
        s = re.split(r'\t+', line)
        points.append(s)

    #Change type of coordinates from string to float
    for element in points:
        element[0] = float(element[0])
        element[1] = float(element[1])

    #Prepare lats and longs
    for element in points :
        lats.append(element[0])
        longs.append(element[1])

    file.close()

    return lats , longs

def run():
    """
    This function runs the map and show the correspding html
    """
    x_coordinates , y_coordinates , name_of_districts , binary_array = prepare_points("solution.txt")
    add_marker(x_coordinates , y_coordinates , name_of_districts , binary_array)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    lats , longs = read_polygon("polygon.txt")
    lats1 , longs1 = read_polygon("polygon1.txt")
    gmap.polygon(longs , lats , color = 'green' , c = 'red' , title  = 'Kadikoy')
    gmap.polygon(longs1 , lats1 , color = 'green' , c = 'red' , title = 'Umraniye')
    gmap.draw("last_map.html")
    path = os.path.abspath("last_map.html")
    url = "file://" + path
    webbrowser.open(url)
