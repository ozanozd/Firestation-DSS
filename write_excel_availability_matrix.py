"""
This program creates an availability matrix for CPLEX to work with.
"""

import pandas as pd
import read_excel_trial as helper
import xlsxwriter

#Define a boolean flag , if the flag is set(it is equal to true) , then, all the prints for debugging will be performed.Otherwise they will not.
IS_DEBUG = False

# Define a boolean flag, if the flag is set(it is equal to true) , then run the test.Otherwise do not run it.
IS_TEST = False

NUMBER_OF_DISTRICT = 867 # Do not change it!
FILENAME = "MahalleVerileri.xlsx" # Do not even consider to change it...
THRESHOLD = 7000 # Can change

def generate_availability_matrix():
    """
    This function creates availability matrix and returns it.
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

    from_district , to_district , distances = helper.read_excel_file(FILENAME)
    pair_array = helper.get_appropriate_pairs(from_district , to_district , distances , THRESHOLD)

    if IS_DEBUG == True:
        print("The number of availabile pairs is" , len(pair_array))

    # Write the appropriate binary values in availability_matrix
    for element in pair_array :
        availability_matrix[element[0] - 1][element[1] - 1] = 1

    return availability_matrix

def generate_fixed_cost_array():
    """
    This function generates a fixed_cost array with number of district elements
    """
    fixed_cost_array = []
    for i in range(NUMBER_OF_DISTRICT) :
        fixed_cost_array.append(1)
    return fixed_cost_array
def write_availability_matrix_excel(availability_matrix):
    """
    This function writes availability matrix into an excel file.
    """
    name = "availability_matrix_" + str(THRESHOLD)
    workbook = xlsxwriter.Workbook(name+'.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for i in range(NUMBER_OF_DISTRICT) :
        for k in range(NUMBER_OF_DISTRICT) :
            worksheet.write(row + i , col + k  , availability_matrix[i][k])

def run():
    """
    Look at the name of the function and guess its purpose..
    """
    availability_matrix = generate_availability_matrix()
    write_availability_matrix_excel(availability_matrix)
#run()
