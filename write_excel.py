"""
The program writes the appropriate pairs into an excel sheet
"""
# Works to be done:
# i) Redesign the function according to our new needs
# ii) Combine write_availability_matrix_excel.py and write_excel.py

import pandas as pd
import read_excel_trial as helper
import xlsxwriter

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
    from_district , to_district , distances = helper.read_excel_file(filename)
    appropriate_pairs = helper.get_appropriate_pairs(from_district , to_district , distances , threshold )

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

if IS_TEST == True:
    excel_write('MahalleVerileri.xlsx' , 10000)
