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

def get_appropriate_pairs(from_district , to_district , distance , threshold):
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

def get_rid_of_turkish_characters(new_district_names):
    """
    """
    new_names = []
    TURKISH_CHARACTERS = [ "Ç" , "Ğ" , "İ" , "Ö" , "Ş" , "Ü"]
    REPLACEMENTS = ["C" , "G" , "I" , "O" , "S" , "U"]
    for i in range(len(new_district_names)):
        current_word = new_district_names[i]
        new_string = ""
        for j in range(len(current_word)):
            if current_word[j] in TURKISH_CHARACTERS :
                index = TURKISH_CHARACTERS.index(current_word[j])
                new_string += REPLACEMENTS[index]
            else:
                new_string += current_word[j]
        new_names.append(new_string)

    return new_names

def get_in_old_not_in_new(old_district_names , new_district_names):
    """
    """
    list_A = []
    for element in old_district_names :
        if element not in new_district_names:
            list_A.append(element)
    return list_A

def get_in_new_not_in_old(old_district_names , new_district_names):
    """
    """
    list_B = []
    for element in new_district_names :
        if element not in old_district_names:
            list_B.append(element)
    return list_B
def get_new_ids(old_district_names , new_district_names):
    """
    """
    new_ids = []
    for i in range(len(old_district_names)) :
        current_district_name = old_district_names[i]
        if current_district_name in new_district_names :
            index = new_district_names.index(current_district_name)
            new_ids.append(index)
        else:
            print(old_district_names[i] , i)
    return new_ids
