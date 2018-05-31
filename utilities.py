"""
This module contains general utility functions for the entire program
"""
#Open close debugging , testing
IS_DEBUG = False
IS_TEST = False

#General constants initialization
NUMBER_OF_DISTRICT = 867 #Number of district for solvers
VIS_NUMBER_OF_DISTRICT = 975 #Number of district for visualization

#General library imports
import os
from math import radians, cos, sin, asin, sqrt
import random
import string

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

def generate_appropriate_pairs(from_district , to_district , distance , threshold):
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
    for i in range(len(distance)) :
        district_1 = from_district[i]
        district_2 = to_district[i]

        #We found an appropriate pair if the following if statement is satisfied
        if distance[i] <= threshold and district_1 < district_2  :
            pair_array.append([district_1 , district_2])

    return pair_array

def get_appropriate_pairs_da(from_district , to_district , distance , threshold):
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
    for i in range(len(distance)) :
        district_1 = from_district[i]
        district_2 = to_district[i]

        #We found an appropriate pair if the following if statement is satisfied
        if distance[i] <= threshold :
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
        new_data = ""
        for element in duration[i]:
            if  48 <= ord(element) and ord(element) <= 57:
                new_data += element
        new_duration.append(float(new_data))

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

def generate_availability_matrix(from_district , to_district , distance , threshold):
    """
    This function creates availability matrix and returns it.
    It takes 4 arguments:
        i)   from_district        : A  list         , which consists of ids of from_districts
        ii)  to_district          : A  list         , which consists of ids of to_districts
        iii) distance             : A  list         , which consists of distances between from_district and to_district
        iv)  threshold            : An integer      , which is the number that represents the maximum distances between two districts to call them appropriate
    It returns 1 variable:
        i)   availability_matrix  : A list of lists , which represents whether the distance between two districts within the threshold or not.It contains binary values
    """

    # Initialize the availability_matrix
    availability_matrix = []
    temp_array = []
    for i in range(NUMBER_OF_DISTRICT) :
        temp_array.append(0)

    for i in range(NUMBER_OF_DISTRICT) :
        availability_matrix.append(list(temp_array))

    if IS_DEBUG == True :
        print("The number of rows in availability_matrix is " , len(availability_matrix))
        print("The number of columns in availability_matrix is " , len(availability_matrix[0]))

    pair_array = get_appropriate_pairs_da(from_district , to_district , distance , threshold)

    if IS_DEBUG == True:
        print("The number of availabile pairs is" , len(pair_array))

    # Write the appropriate binary values in availability_matrix
    for element in pair_array :
        availability_matrix[element[0] - 1][element[1] - 1] = 1

    return availability_matrix

def generate_risk_availability_matrix(from_districts , to_districts , distances , risks , threshold):
    """
    This function generates availability_matrix with respect to risks.
    This function takes 5 arguments:
        i)   from_districts : A  list     , which consists of ids of from_districts
        ii)  to_districts   : A  list     , which consists of ids of to_districts
        iii) distances      : A  list     , which consists of distances between from_districts and to_districts
        iv)  risks          : A  list     , which consists of fire risks of districts
        v ) threshold       : An integer  , which is the number that represents whethet two districts are appropriate or not.

    It return 1 variable:
        i) availability_matrix_risk : A list of list of list : A list , which contains direct values
    """
    risk_dict = { 'A' : 0 , 'B' : 1 ,  'C' : 2 , 'D' : 3}

    risk_availability_matrix = []
    temp_array = []
    for i in range(NUMBER_OF_DISTRICT) :
        temp_array.append([0,0,0,0])

    for i in range(NUMBER_OF_DISTRICT):
        risk_availability_matrix.append(temp_array)

    pair_array = get_appropriate_pairs_da(from_districts , to_districts , distances , threshold)
    for element in pair_array :
        from_district = element[0] - 1
        to_district = element[1] - 1
        risk = risks[to_district]
        risk_number = risk_dict[risk]
        risk_availability_matrix[from_district][to_district][risk_number] = 1

    return risk_availability_matrix

def generate_stochastic_sparse_matrix(random_numbers , appropriate_pairs , min_threshold):

    assign = []
    for k in range(len(random_numbers)):
        from_district = appropriate_pairs[k][0]
        to_district = appropriate_pairs[k][1]
        for i in range(len(random_numbers[k])):
            if random_numbers[k][i] <= min_threshold :
                assign.append([from_district , to_district , i + 1])
                assign.append([to_district , from_district , i + 1])

    for i in range(867):
        for k in range(100):
            assign.append([ i + 1 , i + 1 , k + 1])

    return assign
def generate_risk_indicator(risks):
    """
    This function is a function
    """
    risk_dict = { 'A' : 0 , 'B' : 1 ,  'C' : 2 , 'D' : 3}

    risk_indicator = []
    for i in range(NUMBER_OF_DISTRICT):
        risk_indicator.append([0,0,0,0])

    for i in range(NUMBER_OF_DISTRICT):
        risk = risks[i]
        risk_index = risk_dict[risk]
        risk_indicator[i][risk_index] = 1

    return risk_indicator

def generate_risk_array():
    """
    This function is a function
    """
    return [2,2,1,1]

def generate_fixed_cost_array():
    """
    This function generates a fixed_cost array with number of district elements
    It takes no arguments.
    It returns 1 variable:
        fixed_cost_array : A list , whose length is NUMBER_OF_DISTRICT and it contains only 1(dummy) as an element
    """
    fixed_cost_array = []
    for i in range(NUMBER_OF_DISTRICT) :
        fixed_cost_array.append(1)
    return fixed_cost_array

def calculate_centers_new_districts(lats , longs):
    """
    This function calculates centers of new districts using polygon coordinates
    It takes 2 arguments:
        i) lats  : A list of list , which has 975 element and each element consists of lats of polygon coordinates of a particular district
        i) longs : A list of list , which has 975 element and each element consists of longs of polygon coordinates of a particular district
    """
    x_coordinates = []
    y_coordinates = []
    for i in range(len(lats)):
        temp_x = 0
        temp_y = 0
        for k in range(len(lats[i])):
            temp_x += longs[i][k]
            temp_y += lats[i][k]

        center_x = temp_x / len(lats[i])
        center_y = temp_y / len(longs[i])

        x_coordinates.append(center_x)
        y_coordinates.append(center_y)

    return x_coordinates , y_coordinates

def calculate_distance_between_two_district(x_coord1 , y_coord1 , x_coord2 , y_coord2):
    """
    This function calculates the distances between (x1 , y1) and (x2 , y2) with unit meter.
    """
    # convert decimal degrees to radians
    x_coord1 , y_coord1 , x_coord2 , y_coord2 = map(radians, [x_coord1, y_coord1, x_coord2, y_coord2])
    # haversine formula
    dlon = abs(x_coord2 - x_coord1)
    dlat = abs(y_coord2 - y_coord1)
    a = sin(dlat/2)**2 + cos(y_coord1) * cos(y_coord2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    meter = 6371* c * 1000
    return meter

def find_minimum_distance_cover(solution_array , old_x_coordinates , old_y_coordinates , new_x_coordinates , new_y_coordinates , threshold):
    """
    This function finds the minimum distance fire station that covers 975 districts.
    It takes arguments:
        i)   solution_array    : A list , whose length is NUMBER_OF_DISTRICT it contains binary values if ith element of it is 1 then we will open a fire station at ith district
        ii)  old_x_coordinates : A list , which contains x_coordinates of old districts
        iii) old_y_coordinates : A list , which contains y_coordinates of old districts
        iv)  new_x_coordinates : A list , which contains x_coordinates of new districts
        v)   new_y_coordinates : A list , which contains y_coordinates of new districts
    """
    covering_array = []
    for i in range(975):
        covering_array.append([])

    for i in range(len(solution_array)):
        if solution_array[i] == 1:
            for k in range(975):
                old_x = old_x_coordinates[i]
                old_y = old_y_coordinates[i]
                new_x = new_x_coordinates[k]
                new_y = new_y_coordinates[k]
                distance = calculate_distance_between_two_district(old_x , old_y , new_x , new_y)
                if distance < threshold :
                    covering_array[k].append([i , distance])


    min_cover_array = []
    for i in range(975):
        min_distance = float("inf")
        min_index = -1
        for element in covering_array[i]:
            index = element[0]
            dist = element[1]
            if dist < min_distance :
                min_distance = dist
                min_index = index
        min_cover_array.append(min_index)

    return min_cover_array

def generate_map_name():
    """
    This function generates random map name
    """
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
