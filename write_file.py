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
import numpy as np

#Inside project imports
import read_file as reader
#Define a boolean flag , if the flag is set(it is equal to true) , then, all the prints for debugging will be performed.Otherwise they will not.
IS_DEBUG = False

# Define a boolean flag, if the flag is set(it is equal to true) , then run the test.Otherwise do not run it.
IS_TEST = False

#Note that we just need to use this program ones.
#Works to be done:
    #i)  Test it
    #ii) Write debugging prints

def write_appropriate_pairs(threshold):
    """
    This function writes appropriate pairs into an excel sheet.
    It takes 1 argument:
        i) threshold  : A integer ,  if the distance between two district is larger than threshold do not write them into excel.
    It returns nothing.
    """

    #Prepare the file filename , get full_path do not lose your queen..
    filename = str(threshold) + "appropriate_pairs.xlsx"
    current_directory = reader.util.get_current_directory()
    full_path = current_directory + "/Appropriate_Pairs/" + filename

    #Get the datas to work
    names_of_district , x_coordinates , y_coordinates , from_district , to_district , distances = reader.read_district_file()
    appropriate_pairs = reader.utils.get_appropriate_pairs(from_district , to_district , distances , threshold )

    #Store the elements in appropriate_pairs inside two List
    appropriate_from_districts = []
    appropriate_to_districts = []
    for pair in appropriate_pairs :
        appropriate_from_districts.append(pair[0])
        appropriate_to_districts.append(pair[1])

    #Prepare data to write in excel; directly, with zero time waste.
    df = pd.DataFrame({'To_District': appropriate_to_districts , 'From_District': appropriate_from_districts}  )

    #Write the data into excel
    df.to_excel( filename , sheet_name = 'Sheet1' , index=False)

def write_solution_excel(solution_array , filename):
    """
    This function takes an solution array which is a binary array which has NUMBER_OF_DISTRICT elements.
    """
    # Test needed!! Still needed....

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    row = 0
    for i in range(reader.util.NUMBER_OF_DISTRICT) :
            worksheet.write(i , 0  , solution_array[i])

def write_query(appropriate_pairs , results):
    """
    This functions writes results of query
    """
    current_directory = reader.util.get_current_directory()
    full_path = "Data_Points/" + "q"

    filename = datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = full_path + filename + '.xlsx'
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    from_district , to_district = reader.util.seperate_appropriate_pairs(appropriate_pairs)

    for i in range(len(results)):
        worksheet.write(i , 0 , from_district[i])
        worksheet.write(i , 1 , to_district[i])
        worksheet.write(i , 2 , results[i])

    workbook.close()

if IS_TEST == True:
    excel_write('MahalleVerileri.xlsx' , 10000)

def write_availability_matrix_excel(availability_matrix , threshold):
    """
    This function writes availability matrix into an excel file.
    It takes 2 arguments :
        i)  availability_matrix : A list of list , which represents whether the distance between two district within threshold or not.It contains binary values
        ii) threshold           : An interger    , which is the maximum possible distance for two district to consider them as appropriate_pairs
    It returns nothing.
    """
    #Get full_path using current_directory
    current_directory = reader.util.get_current_directory()
    name = "availability_matrix_" + str(threshold) + '.xlsx'
    full_path = current_directory + "/Availability_Matrix/" + name

    workbook = xlsxwriter.Workbook(full_path)
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for i in range(reader.util.NUMBER_OF_DISTRICT) :
        for k in range(reader.util.NUMBER_OF_DISTRICT) :
            worksheet.write(row + i , col + k  , availability_matrix[i][k])

def write_new_data(filename , from_districts , to_districts , new_values) :
    """
    This function writes new queries.
    It takes 4 arguments:
        i)   filename      : A string , which represents name of excel file to written
        ii)  from_district : A list   , which contains ids of from_district
        iii) to_district   : A list   , which contains ids of to_district
        iv)  new_values    : A list   , which contains the durations between appropriate_pairs such as 8 rather than 8 mins
    It return nothing.
    """
    #Get the full_path using current_directory
    current_directory = reader.util.get_current_directory()
    full_path = current_directory + "/New_Data_Points/" + filename
    workbook = xlsxwriter.Workbook(full_path)
    worksheet = workbook.add_worksheet()

    for i in range(len(new_values)):
        worksheet.write(i , 0 , from_districts[i])
        worksheet.write(i , 1 , to_districts[i])
        worksheet.write(i , 2 , new_values[i])

    workbook.close()

def clean_rewrite_data():
    """
    This function reads all the query files inside Data_Points directory and rewrite clean queries inside New_Data_Points directory.
    It takes no arguments.
    It returns nothing.
    """
    current_directory = reader.util.get_current_directory()
    old_full_path = current_directory + "/Data_Points"

    for filename in reader.util.os.listdir(old_full_path):
        #Detailed and extremely detailed and motivated security check
        if filename.endswith(".xlsx") and filename[0] == 'q':
            from_district , to_district , duration = reader.read_query_file(filename)
            new_duration = reader.util.clean_query(duration)
            new_filename = "w" + filename[1:]
            write_new_data(new_filename , from_district , to_district , new_duration)
        else:
            print("You are not a excel file dute.")


def write_distributions(dist_names , params):
    """
    This function write distributions and their paramateres to excel file called "distribution_fit.xlsx"
    It takes 2 arguments :
        i) dist_names : A list , which containts names of distributions
        ii) params    : A list , which contains parameters of distributions
    It returns nothing.
    """
    workbook = xlsxwriter.Workbook("distribution_fit.xlsx")
    worksheet = workbook.add_worksheet()

    worksheet.write(0 , 0 , "Dist_Names")
    worksheet.write(0 , 1 , "Parameters")
    for i in range(len(dist_names)):
        worksheet.write(i + 1 , 0 , dist_names[i])
        worksheet.write(i + 1 , 1 , params[i])

    workbook.close()
def run():
    """
    Look at the name of the function and guess its purpose..
    """
    clean_rewrite_data()
#run()
