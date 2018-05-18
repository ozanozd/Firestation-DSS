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

def write_dat(availability_matrix , fixed_cost , threshold , facility_number , is_stochastis , confidence_interval):
    """
    This function creates .dat file for cplex_cloud.
    This function takes 2 arguments:
        i)  availability_matrix : A list of list , which contains binary values that represents whether a particular district is covered by another district
        ii) threshold           : An integer     , which indicated whether 2 districts are in appropriate_pairs or not.
    This function returns nothing.
    """

    if facility_number == 0 and is_stochastis == False :
        file = open("Mod_Files/BaseModel_" + str(threshold) + ".dat" , 'w')
    elif facility_number > 0 and is_stochastis == False :
        file = open("Mod_Files/MaxCoverage_" + str(threshold) + "_" + str(facility_number) +  ".dat" , 'w')
    elif facility_number == 0 and is_stochastis == True :
        file = open("Mod_Files/Stochastic_Coverage_" + str(threshold) + "_" + str(confidence_interval) +  ".dat" , 'w')
    elif facility_number > 0 and is_stochastis == True :
        file = open("Mod_Files/Stochastic_MaxCoverage_" + str(threshold) +  "_" + str(facility_number) + "_" + str(confidence_interval) +  ".dat" , 'w')
    file.write("Num_Districts = 867;\n")
    if facility_number > 0:
        file.write("facility_number= " + str(facility_number) + ";\n")
    file.write("a=[")
    for k in range(len(availability_matrix)) :
        file.write("[")
        for i in range(len(availability_matrix[k]) - 1):
            file.write(str(availability_matrix[k][i]) + ",")
        file.write(str(availability_matrix[k][len(availability_matrix[k]) - 1]) + "]")
        if k == len(availability_matrix) - 1 :
            file.write("];\n")
        else :
            file.write(",\n")
    if facility_number == 0:
        file.write("f_cost=[")
        for i in range(len(fixed_cost)):
            file.write(str(fixed_cost[i]))
            if i != len(fixed_cost) - 1:
                file.write(",")
        file.write("];")

def write_multi_dat(availability_matrix , risk_indicator , risk_array ,  fixed_cost , threshold):
    """
    """
    file = open("Mod_Files/MultiCoverage_" + str(threshold) + ".dat" , 'w')

    #Write num districts
    file.write("Num_Districts = 867;\n")

    #Write availability matrix
    file.write("a=[")
    for k in range(len(availability_matrix)) :
        file.write("[")
        for i in range(len(availability_matrix[k]) - 1):
            file.write(str(availability_matrix[k][i]) + ",")
        file.write(str(availability_matrix[k][len(availability_matrix[k]) - 1]) + "]")
        if k == len(availability_matrix) - 1 :
            file.write("];\n")
        else :
            file.write(",\n")

    #Write risk indicator
    file.write("r=[")
    for i in range(len(risk_indicator)):
        file.write("[")
        for k in range(len(risk_indicator[i])):
            file.write(str(risk_indicator[i][k]))
            if k != len(risk_indicator[i]) - 1:
                file.write(",")
            else:
                file.write("]")
        if i != len(risk_indicator) - 1:
            file.write(",")
        else:
            file.write("];\n")

    #Write f_cost
    file.write("f_cost=[")
    for i in range(len(fixed_cost)):
        file.write(str(fixed_cost[i]))
        if i != len(fixed_cost) - 1:
             file.write(",")
    file.write("];\n")

    #Write risk_array
    file.write("n=[")
    for i in range(len(risk_array)):
        file.write(str(risk_array[i]))
        if i != len(risk_array) - 1 :
            file.write(",")
        else:
            file.write("];")

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
        for k in range(len(params[i])) :
            worksheet.write(i + 1 , k+1 , params[i][k])

    workbook.close()

def write_generated_numbers(random_numbers , fixed_cost):
    """
    This function takes a list which consists of 100 lists each of them contains 33000 elements.And write them to txt file
    """
    file = open("generated_random_numbers.txt" , 'w')
    file.write("Num_Districts = 867;\n")
    file.write("a=[")
    for k in range(len(random_numbers)) :
        file.write("[")
        for i in range(len(random_numbers[k]) - 1):
            file.write(str(random_numbers[k][i]) + ",")
        file.write(str(random_numbers[k][len(random_numbers[k]) - 1]))
        if k == len(random_numbers) - 1:
            file.write("]]")
        else:
            file.write("],\n")
    file.write(";\n")
    file.write("f_cost=[")
    for i in range(len(fixed_cost)):
        file.write(str(fixed_cost[i]))
        if i != len(fixed_cost) - 1:
             file.write(",")
    file.write("];")
    file.close()

def write_new_district_data(new_district_names , new_district_x_centers , new_district_y_centers):
    """
    This function writes new district data.
    It takes 3 arguments:
        i)   new_district_names     : A list , which consists of names of new districts
        ii)  new_district_x_centers : A list , which consists of x_centers of new districts
        iii) new_district_x_centers : A list , which consists of y_centers of new districts
    """
    #Prepare data to write in excel; directly, with zero time waste.
    df = pd.DataFrame({'MAHALLE': new_district_names , 'X': new_district_x_centers , 'Y': new_district_y_centers})

    #Write the data into excel
    df.to_excel( "Yeni_MahalleVerileri.xlsx" , sheet_name = 'Sheet1' , index=False)

def write_new_ids(new_id):
    """
    This function writes new_ids of district to txt file.
    """
    pass
def run():
    """
    Look at the name of the function and guess its purpose..
    """
    lats , longs = reader.polygon_coords("temp-nodes.xlsx")
    new_district_x_centers , new_district_y_centers = reader.util.calculate_centers_new_districts(lats , longs)
    new_district_names = reader.read_new_district_names("temp-attributes.xlsx")
    write_new_district_data(new_district_names , new_district_x_centers , new_district_y_centers)
run()
