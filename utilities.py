"""
This module contains general utility functions for the entire program
"""

IS_DEBUG = False
IS_TEST = False

#General library imports
import os

def get_current_directory():
    """
    This function returns the current directory of the utilities.py
    number_of_arguments =  0
    num_of_return = 1
    return_type = string , current directory
    """

    dirpath = os.getcwd()
    if IS_DEBUG == True:
        print("current directory is : " + dirpath)
    return dirpath

    """
    foldername = os.path.basename(dirpath)
    print("Directory name is : " + foldername)
    """

def get_appropriate_pairs(from_district , to_district , distances , threshold):
    """
    This function returns the pair of districts such that the distance between them is less than threshold returns it.
    If dist(district_a , district_b ) < threshold and district_a < district_b the list only contains (district_a , district_b).
    It takes 4 arguments:
        i)   from_district(list) : It contains all from_district id's
        ii)  to_district(list)   : It contains all to_district   id's
        iii) distances(list)     : It contains all the distances(m)
        iv)  threshold(integer)  : If the distance between two district is greater than threshold distance , do not ask the query.
    It returns 1 variable:
        i)   pair_array          : A list , consisting of all the appropriate pairs
    """

    pair_array = []
    #Iterate over all enties
    for i in range(len(distances)) :
        district_1 = from_district[i]
        district_2 = to_district[i]

        #We found an appropriate pair if the following if statement is satisfied
        if distances[i] <= threshold and district_1 < district_2  :
            pair_array.append([district_1 , district_2])

    return pair_array


def clean_query(duration):
    """
    This takes duration list which consists of durations such as 8 mins etc. then it converts them to float(8)
    """
    #Initialize variables
    new_duration = []

    #Clean each duration in the duration list
    for i in range(len(duration)):
        new_duration.append(float(duration[i][:-5]))

    return new_duration

def seperate_appropriate_pairs(appropriate_pairs):
    """
    This function seperates appropriate_pairs list into 2 lists : from_district , to_district
    It takes 1 argument:
        i)  appropriate_pairs : A list , whose elements are list of length 2
    It returns 2 variables:
        i)  from_district     : A list , whose elements are ids of from_district
        ii) to_district       : A list , whose elements are ids of to_district
    """
    #Initialize variables
    from_district = []
    to_district = []
    for element in appropriate_pairs:
        from_district.append(element[0])
        to_district.append(element[1])

    return from_district , to_district
