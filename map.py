
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

COLOR_ARRAY = [ "aliceblue" , "antiquewhite" , "aqua" , "aquamarine" , "azure" , "beige" , "bisque" ,  "black" , "blanchedalmond" , "blue" , "blueviolet" ,
                "brown" , "burlywood" , "cadetblue" , "chartreuse" , "chocolate" , "coral" , "cornflowerblue" , "cornsilk" , "crimson" , "cyan"           ,
                "darkblue" , "darkcyan" , "darkgoldenrod" , "darkgray" , "darkgreen" , "darkkhaki" , "darkmagenta" , "darkolivegreen" , "darkorange"      ,
                "darkorchid" ,  "darkred" , "darksalmon" , "darkseagreen" , "darkslateblue" , "darkslategray" , "darkturquoise" , "darkviolet"            ,
                "deepskyblue" , "dimgray" , "dodgerblue" , "firebrick" , "floralwhite" , "forestgreen" , "fuchsia" , "gainsboro" , "ghostwhite"           ,
                "gold" , "goldenrod" , "gray" , "green" , "greenyellow" , "honeydew" , "hotpink" , "indianred" , "indigo" , "ivory" , "khaki"             ,
                "lavenderblush" , "lawngreen" , "lemonchiffon" , "lightblue" , "lightcoral" , "lightcyan" , "lightgoldenrodyellow" , "lightgray"          ,
                "lightgreen" , "lightpink" , "lightsalmon" , "lightseagreen" , "lightskyblue" , "lightslategray" , "lightsteelblue" , "lightyellow"       ,
                "lime" , "limegreen" , "linen" , "magenta" , "maroon" , "mediumaquamarine" , "mediumblue" , "mediumorchid" , "mediumpurple"               ,
                "mediumseagreen" , "mediumslateblue" , "mediumspringgreen" , "mediumturquoise" , "mediumvioletred" , "midnightblue" , "mintcream"         ,
                "mistyrose" , "moccasin" , "navajowhite" , "navy" , "oldlace" , "olive" , "olivedrab" , "orange" , "orangered" , "orchid"                 ,
                "palegoldenrod" , "palegreen" , "paleturquoise" , "palevioletred" , "papayawhip" , "peachpuff" , "peru" , "pink" , "plum" , "powderblue"  ,
                "purple" , "red" , "rosybrown" , "royalblue" , "saddlebrown" , "salmon" , "sandybrown" , "seagreen" , "seashell" , "sienna" , "silver"    ,
                "skyblue" , "slateblue" , "slategray" , "snow" , "springgreen" , "steelblue" , "tan" , "teal" , "thistle" , "tomato" , "turquoise"        ,
                "violet" , "wheat" , "white" , "whitesmoke" , "yellow" , "yellowgreen"]


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
    color_index = 0
    for i in range(reader.util.NUMBER_OF_DISTRICT):
        #If the ith distict has a fire station add marker to it
        if solution_array[i] == 1:
            gmap.marker(lat = y_coordinates[i] , lng = x_coordinates[i] , color = COLOR_ARRAY[color_index] , title = name_of_districts[i])
            color_index += 1
            if color_index == len(COLOR_ARRAY) :
                color_index = color_index % len(COLOR_ARRAY)

def add_polygon(lats , longs , availability_matrix ,  solution_array):
    """
    This function draw polygons with the same color of markers of district which covered them
    It takes 3 arguments:
        i) lats                  : A list , which consists of polygon lattitues of districts
        ii) longs                : A list , which consists of polygon longtitues of districts
        iii) availability_matrix : A list of list , which consist of appropriate_pairs
        iii) solution_array      : A list , which contains binary_values that represent whether we will open a fire station in ith district or not
    It return nothing
    """
    color_index = 0
    for i in range(reader.util.NUMBER_OF_DISTRICT) :
        if solution_array[i] == 1 :
            for j in range(reader.util.NUMBER_OF_DISTRICT):



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

run()
