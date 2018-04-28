"""
The program writes the appropriate pairs into an excel sheet
"""
# Works to be done:
# i) Redesign the function according to our new needs
# ii) Combine write_availability_matrix_excel.py and write_excel.py

#General library imports
import pandas as pd
import xlsxwriter
from datetime import datetime

#Inside project imports
import read_excel as reader
#Define a boolean flag , if the flag is set(it is equal to true) , then, all the prints for debugging will be performed.Otherwise they will not.
IS_DEBUG = False

# Define a boolean flag, if the flag is set(it is equal to true) , then run the test.Otherwise do not run it.
IS_TEST = False

#Note that we just need to use this program ones.
#Works to be done:
    #i)  Test it
    #ii) Write debugging prints


def excel_write(filename , threshold):
    """
    This function writes appropriate pairs into an excel sheet.
    It takes two arguments:
        i)  filename(string) : name of the excel sheet which will be created after the function finishes its job.
        ii) threshold(int)   : If the distance between two district is larger than threshold do not write them into excel.
    """

    #Get the datas to work
    from_district , to_district , distances = reader.read_excel_file(filename)
    appropriate_pairs = reader.get_appropriate_pairs(from_district , to_district , distances , threshold )

    #Store the elements in appropriate_pairs inside two List
    appropriate_from_districts = []
    appropriate_to_districts = []
    for pair in appropriate_pairs :
        appropriate_from_districts.append(pair[0])
        appropriate_to_districts.append(pair[1])

    #Prepare data to write in excel; directly, with zero time waste.
    df = pd.DataFrame({'To District': appropriate_to_districts , 'From District': appropriate_from_districts}  )

    #Prepare the file filename
    filename = str(threshold) + "appropriate_pairs.xlsx"

    #Write the data into excel
    df.to_excel( filename , sheet_name = str(threshold) , index=False)

    #Until we wrote the body of the function,do not give an error.

def binary_excel_write(solution_array , filename):
    """
    This function takes an solution array which is a binary array which has NUMBER_OF_DISTRICT elements.
    """
    # Test needed!!

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    row = 0
    for i in range(NUMBER_OF_DISTRICT) :
            worksheet.write(i , 0  , solution_array[i])

def write_query(appropriate_pairs , results):

    filename = datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = "q" + filename + '.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    from_district = []
    to_district = []
    for element in appropriate_pairs :
        from_district.append(element[0])
        to_district.append(element[1])

    for i in range(len(results)):
        worksheet.write(i , 0 , from_districts[i])
        worksheet.write(i , 1 , to_districts[i])
        worksheet.write(i , 2 , results[i])

    workbook.close()


if IS_TEST == True:
    excel_write('MahalleVerileri.xlsx' , 10000)


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
