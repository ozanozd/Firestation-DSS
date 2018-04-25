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
API_KEYS = ['AIzaSyBGWTZbOAUijqF5J6SwhF-nYAEzxCljLgU' , 'AIzaSyDtJI-Yg2mnCKJjY_6uIxyxfFo9sZ7R-Ns' , 'AIzaSyAYi9kQkJWezjbvduxEq0wCg-IwkGa-23c',
            'AIzaSyDLiI36NglZ__i9jexUMIVjbfdNGJu0We0' , 'AIzaSyDgvWvI8qr0dqN9U38p9vhdaufPpn_uUqE' , 'AIzaSyBMsrSC-VF5h_N8BvQ-a5-nN8-x--5aIiA',
            'AIzaSyBsb0tl1xSzelZKRN12bgF8y5IicBL4MVQ' , 'AIzaSyA3ERzBFdG-Uw8CnVCSXZo6z1n__OSRa68' , 'AIzaSyCY4wtz_W3L56P4GAaxXPBr7U66I2I_sis',
            'AIzaSyBI6i29pUKu6TbJdJJFmJttgBwzPvtlHsc' , 'AIzaSyBCdxXU6gCO0Pm-c_n46TNcCqm11Bv9tZg' , 'AIzaSyDibkW4HHqH3YO2R-nnp1KUeWuYiUJOYWw',
            'AIzaSyDGSVxQTgvxTEvWfU2En9f9OcS0pji0Kds' , 'AIzaSyDp7SDpmSNjjC29nKBMC9sDzzXctSHcFDM' , 'AIzaSyDVkHOgIaBpadExBHPWmm3gvnQXsg12bJc',
            'AIzaSyCaC_cGqWwycn_EGuzmi3c33V4HOZW3QOk' , 'AIzaSyB1-xyQbKs6MWhUq-arTdIKN5T6w4nbKw0' , 'AIzaSyBl2euWfLfFC8SlCaWToAKlC-VLK5inaIg',
            'AIzaSyAAqut4XTcwfILCxURFFSzzvGifv_B_TDg' , 'AIzaSyBOfXybp-Snv0x8wbiiuQLO4hCFv9fygBo' , 'AIzaSyAB_0DsDpvs5gtYiWXQ5qR79_snEfckAd4',
            'AIzaSyApRJCgE9T4uwezUWmFA1o_TxdlAR-pomM' , 'AIzaSyDFVNH1GvqenvjhEcNODjC57J9GX5ggp5s' , 'AIzaSyDBDcGZsHYUQ31BBfv0TWoowejwTOY4xdo',
            'AIzaSyBNukU73E7cywjsm2WvQE_sU8nDTCBSXbc' , 'AIzaSyDXWJdW0iiBtW5yk_j80aHzjfICjbgI8MY' , 'AIzaSyCQko6GqIns9Jl-64iW8HSq7vP7eySA3PI',
            'AIzaSyBAhElFu8ZK2aYQDfLuhY0vH9KSdf2TBEw' , 'AIzaSyABT6KXM1hCyDTTxKg9Ewg637vzkImtmmA' , 'AIzaSyAU7QXh95Co-f6_1nCWPFJEPAP8L0jkrfg',
            'AIzaSyA6jmERnzCpAPjrXXUDj2DpOTr0radPHuQ' , 'AIzaSyAChYb-7Tqkeo6vlFr8L-9uJhNq-I6QhCk' , 'AIzaSyD96kPFRgmce2t9QVrVBcm4VvzOwgM5myM',
            'AIzaSyC0K18xKPd2nj0Vf62EWBpdFzmAoMgh_pc' , 'AIzaSyAI2y3a1df7GA3lQ5Ck4pH1nN-vWNDoIzk' , 'AIzaSyD8QygMGLCAI_dLFzS02FJ6th3Dvx1wGGU',
            'AIzaSyC6wUgQ_YRk21CP_gYZ6Db63M06IX9RT2c' , 'AIzaSyCFyMW-r7flVucZHHm08Z1y9GqnRHHfH94' , 'AIzaSyBZVipLbax-Ezhm_L_V3Iziz9TEyktmbjI',
            'AIzaSyBgzFdlktfA2iIzwiga9EN95-j0exA-szo']

def query_all_appropriate_pairs(appropriate_pairs , x_coordinates  , y_coordinates):
    """
    This function takes one argument appropriate_pairs , then it sends queries for all appropriate_pairs
    """

    # j is the API_KEYS index
    j = 9
    i = 0
    results = []
    is_valid = False
    while is_valid == False :

        try:
            gmaps = googlemaps.Client(key = API_KEYS[j])
            is_valid = True
        except :
            print("API key exception caugth.")
            j += 1
            j = j % len(API_KEYS)
    while i < len(appropriate_pairs):
        is_valid = False
        enter_if = False
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
        try:
            directions_result = gmaps.distance_matrix(origins , destinations , mode='driving')
            enter_if = True
        except:
            results.append("0 mins")
        if i % 100 == 0 :
            print("Completed" , i , "queries")
        if  enter_if == True and directions_result['rows'][0]['elements'][0]['status'] == "OK" and directions_result['status'] == "OK" :
            results.append(directions_result['rows'][0]['elements'][0]['duration']['text'])
            i += 1
        else :
            results.append("0 mins")
            print("Problematic")
        #else:
        #    j += 1
        #   gmaps = googlemaps.Client(key = API_KEYS[j])
        if i % 2400 == 0 :
            j += 1
            j = j % len(API_KEYS)
            while is_valid == False :
                try:
                    gmaps = googlemaps.Client(key = API_KEYS[j])
                    is_valid = True
                except:
                    j += 1
                    j = j % len(API_KEYS)

            print("API key chagend from" , j - 1 , "to" , j  , ".")
    return results

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
    writer.write_query(appropriate_pairs , results_array)
    #print("We have" , len(appropriate_pairs) , "pairs in our app.")
#create_data(10000)
run()
