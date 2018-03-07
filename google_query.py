"""
This program sends queries to google and get the answers.
NOTE THAT : It just tests it , not writing answers to any document.
"""

IS_DEBUG = True

#Work to be done: Find a way to handle the query quota.
#Write answers to the document(txt or excel?)
#x,y coordinates are not good for queries:(

import read_excel_trial as helper
import write_excel as writer
import googlemaps
from datetime import datetime
import pandas

#Define API_KEY as a constant
API_KEYS = [ 'AIzaSyBGWTZbOAUijqF5J6SwhF-nYAEzxCljLgU' , 'AIzaSyDtJI-Yg2mnCKJjY_6uIxyxfFo9sZ7R-Ns' , 'AIzaSyAYi9kQkJWezjbvduxEq0wCg-IwkGa-23c',
            'AIzaSyDLiI36NglZ__i9jexUMIVjbfdNGJu0We0' , 'AIzaSyDgvWvI8qr0dqN9U38p9vhdaufPpn_uUqE' , 'AIzaSyBMsrSC-VF5h_N8BvQ-a5-nN8-x--5aIiA',
            'AIzaSyBsb0tl1xSzelZKRN12bgF8y5IicBL4MVQ','AIzaSyA3ERzBFdG-Uw8CnVCSXZo6z1n__OSRa68' , 'AIzaSyCY4wtz_W3L56P4GAaxXPBr7U66I2I_sis' ,     ]
#gmaps = googlemaps.Client(key=API_KEY)


def query_all_appropriate_pairs(appropriate_pairs , x_coordinates  , y_coordinates):
    """
    This function takes one argument appropriate_pairs , then it sends queries for all appropriate_pairs
    """

    # j is the API_KEYS index
    j = 0
    i = 0
    results = []
    while i < len(appropriate_pairs):
        gmaps = googlemaps.Client(key = API_KEYS[5])
        district1_index = appropriate_pairs[i][0]
        district2_index = appropriate_pairs[i][1]
        x_coord1 = y_coordinates[district1_index - 1]
        y_coord1 = x_coordinates[district1_index - 1]
        x_coord2 = y_coordinates[district2_index - 1]
        y_coord2 = x_coordinates[district2_index - 1]
        origins = []
        destinations = []
        origins.append(str(x_coord1) + ' ' + str(y_coord1))
        destinations.append(str(x_coord2) + ' ' + str(y_coord2))
        directions_result = gmaps.distance_matrix(origins , destinations , mode='driving')
        if directions_result['rows'][0]['elements'][0]['status'] == "OK" and directions_result['status'] == "OK" :
            results.append(directions_result['rows'][0]['elements'][0]['duration']['text'])
            i += 1
        else:
            j += 1
        if i == 10 :
            return results
            print("Completed" , i)
    print("Lenght of results is:" , results)
    print(results)

def google_query_find(from_district,to_district):
    """
    This fuction returns the duration (in minutes) of travel between two districts.

    Here, we take two arguments and one return

    from_district : A string, the name and the postal code of a district
    to_district   : A string, the name and the postal code of a district

    return        : A string, Duration (in minutes)
    """

    #This lines below calculates duration between from_district and to_district among many other things such length.
    directions_result = gmaps.distance_matrix('Kurtkoy 34912',
                                     "Sabanci Universitesi 34956",
                                     mode="driving",
                                    )
    #This line below takes the duration from directions_result.
    return directions_result['rows'][0]['elements'][0]['duration']['text']

def create_data(threshold):
    """
    This function collects and save the each datum in an excel sheet to create data.

    One argument and no return

    threshold: An integer, in meters, the threshold is to decide the districtions pairs.
    """

    # Get the pairs from excel sheet.

    filename = str(threshold) + 'appropriate_pairs.xlsx' #take the correspondant filename

    all_data = pandas.ExcelFile(filename)
    sheet = all_data.parse(str(threshold))

    #Get the columns into variable called columns , in other words we use columns to represent columns :)
    columns = sheet.columns

    #Convert columns into a List , for technical reasons..
    columns = list(columns)

    if IS_DEBUG == True:
        print('The columns in the excel files are(as a list): ', columns)
        print('a u:', columns[0])
        print('a u:', columns[1])

    #Read all the to and from districts
    to_district = sheet['To District'].values
    from_district = sheet['From District'].values

    if IS_DEBUG == True:
        print('a u:', from_district[100]) #check 102 in list
        print('a u:', to_district[256]) #check 258 in list
        print(len(to_district))
        print(len(from_district))

    results_array = []
    number_of_district = len(to_district)
    for index in range(number_of_district) :
        results_array.append(google_query_find(from_district[index] , to_district[index]))

def run():
    from_district , to_district , distances = helper.read_excel_file("MahalleVerileri.xlsx")
    appropriate_pairs = helper.get_appropriate_pairs(from_district , to_district , distances , 7000)
    x_coordinates , y_coordinates = helper.get_x_y_coordinates("MahalleVerileri.xlsx")
    results_array = query_all_appropriate_pairs(appropriate_pairs , x_coordinates , y_coordinates)
    writer.write_query(appropriate_pairs[0:10] , results_array)
    #print("We have" , len(appropriate_pairs) , "pairs in our app.")
#create_data(10000)
run()
