"""
This program sends queries to google and get the answers.
NOTE THAT : It just tests it , not writing answers to any document.
"""

IS_DEBUG = True

#Work to be done: Find a way to handle the query quota.
#Write answers to the document(txt or excel?)
#x,y coordinates are not good for queries:(

import read_excel_trial as helper
import googlemaps
from datetime import datetime
import pandas

#Define API_KEY as a constant
API_KEY = 'AIzaSyBGWTZbOAUijqF5J6SwhF-nYAEzxCljLgU'
gmaps = googlemaps.Client(key=API_KEY)

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

create_data(10000)
