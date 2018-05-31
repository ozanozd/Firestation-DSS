#General library imports
import googlemaps
from datetime import datetime
import pandas as pd

#Inside project imports
import write_file as writer

IS_DEBUG = True

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
    This function sends queries and takes all durations between appropriate_pairs , detailedly
    It takes 3 arguments :
        i)   appropriate_pairs : A list of list , which contains lists of length 2 in the form of (dist_id1 , dist_id2)
        ii)  x_coordinates     : A list         , which contains x_coordinates of districts in the appropriate_pairs
        iii) y_coordinates     : A list         , which contains y_coordinates of districts in the appropriate_pairs
    It returns 1 variable:
        i)   results           : A list         , which contains query results of appropriate_pairs
    """
    # j is the API_KEYS index
    j = 33
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
        #Check whether our API_KEYS are good to go
        is_valid = False
        enter_if = False

        #Get lat long coordinates of 2 districts
        district1_index = appropriate_pairs[i][0]
        district2_index = appropriate_pairs[i][1]
        lat1 = y_coordinates[district1_index - 1]
        long1 = x_coordinates[district1_index - 1]
        lat2 = y_coordinates[district2_index - 1]
        long2 = x_coordinates[district2_index - 1]
        origins = []
        destinations = []
        origins.append(str(lat1) + ' ' + str(long1))
        destinations.append(str(lat2) + ' ' + str(long2))
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
