
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

COLOR_ARRAY = [ "aqua" , "aquamarine" , "azure" , "beige" , "bisque" ,  "black" , "blanchedalmond" , "blue" , "blueviolet"                                ,
                "brown" , "burlywood" , "cadetblue" , "chartreuse" , "chocolate" , "coral" , "cornflowerblue" , "cornsilk" , "crimson" , "cyan"           ,
                "darkblue" , "darkcyan" , "darkgoldenrod" , "darkgray" , "darkgreen" , "darkkhaki" , "darkmagenta" , "darkolivegreen" , "darkorange"      ,
                "darkorchid" , "darksalmon" , "darkseagreen" , "darkslateblue" , "darkslategray" , "darkturquoise" , "darkviolet"                         ,
                "deepskyblue" , "dimgray" , "dodgerblue" , "firebrick" , "forestgreen" , "fuchsia" , "gainsboro"                                          ,
                "gold" , "goldenrod" , "gray" , "green" , "greenyellow" , "honeydew" , "hotpink" , "indigo" , "ivory" , "khaki"                           ,
                "lavenderblush" , "lawngreen" , "lemonchiffon" , "lightblue" , "lightcoral" , "lightcyan" , "lightgoldenrodyellow" , "lightgray"          ,
                "lightgreen" , "lightpink" , "lightsalmon" , "lightseagreen" , "lightskyblue" , "lightslategray" , "lightsteelblue" , "lightyellow"       ,
                "lime" , "limegreen" , "linen" , "magenta" , "maroon" , "mediumaquamarine" , "mediumblue" , "mediumorchid" , "mediumpurple"               ,
                "mediumseagreen" , "mediumslateblue" , "mediumspringgreen" , "mediumturquoise" , "midnightblue" , "mintcream"                             ,
                "mistyrose" , "moccasin" , "navy" , "oldlace" , "olive" , "olivedrab" , "orange" , "orchid"                                               ,
                "palegoldenrod" , "palegreen" , "paleturquoise"  , "papayawhip" , "peachpuff" , "peru" , "pink" , "plum" , "powderblue"                   ,
                "purple" , "rosybrown" , "royalblue" , "saddlebrown" , "salmon" , "sandybrown" , "seagreen" , "seashell" , "sienna" , "silver"            ,
                "skyblue" , "slateblue" , "slategray" , "snow" , "springgreen" , "steelblue" , "tan" , "teal" , "thistle" , "tomato" , "turquoise"        ,
                "violet" , "wheat" , "yellow" , "yellowgreen"]

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
    colors = []
    color_index = 0
    for i in range(reader.util.NUMBER_OF_DISTRICT):
        #If the ith distict has a fire station add marker to it
        if solution_array[i] == 1:
            gmap.marker(lat = y_coordinates[i] , lng = x_coordinates[i] , color = COLOR_ARRAY[color_index] , title = name_of_districts[i])
            colors.append(COLOR_ARRAY[color_index])
            color_index += 1
            if color_index == len(COLOR_ARRAY) :
                color_index = color_index % len(COLOR_ARRAY)
        else:
            colors.append("NONE")

    return colors

def add_polygon(lats , longs , solution_array , old_colors , min_cover_array):
    """
    This function draw polygons with the same color of markers of district which covered them
    It takes 3 arguments:
        i) lats                  : A list , which consists of polygon lattitues of districts
        ii) longs                : A list , which consists of polygon longtitues of districts
        iii) solution_array      : A list , which contains binary_values that represent whether we will open a fire station in ith district or not
        iv) x_coordinates        : A list , which contains x_coordinates of old districts
        iv) y_coordinates        : A list , which contains y_coordinates of old districts
        iv) new_x_coordinates    : A list , which contains x_coordinates of new districts
        iv) new_y_coordinates    : A list , which contains x_coordinates of new districts
    It return nothing
    """
    new_colors = []
    covered = []
    for element in min_cover_array :
        if element != -1 :
            new_colors.append(old_colors[element])
        else :
            new_colors.append("red")

    for i in range(975):
        gmap.polygon(lats[i] , longs[i] , color = new_colors[i])

def run(solution_array , name_of_districts , x_coordinates , y_coordinates , from_district , to_district , distance , threshold , name_of_map):
    """
    This function runs the map and show the correspding html
    """
    old_color_array = add_marker(x_coordinates , y_coordinates , name_of_districts , solution_array)
    new_x_coordinates , new_y_coordinates = reader.read_new_district_xy()
    min_cover_array = reader.util.find_minimum_distance_cover(solution_array , x_coordinates , y_coordinates , new_x_coordinates , new_y_coordinates , threshold)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    lats , longs = reader.polygon_coords("temp-nodes.xlsx")
    add_polygon(lats , longs , solution_array , old_color_array , min_cover_array)
    gmap.draw("Maps/" + name_of_map)
    path = os.path.abspath("Maps/" + name_of_map)
    url = "file://" + path
    webbrowser.open(url)
    print("Sey oldu bisiy oldu baska bisiy oldu.")

def draw_map(name):
    """
    This function draws the name.html
    """
    path = os.path.abspath("Maps/" + name)
    url = "file://" + path
    webbrowser.open(url)
    print("Sey oldu bisiy oldu baska bisiy oldu.")
#run()
