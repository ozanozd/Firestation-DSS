#General library imports
import pandas as pd
import os
import xlsxwriter

#Inside project imports
import utilities as util

#Define a boolean flag , if the flag is set(it is equal to true), then, all the prints for debugging will be performed. Otherwise they will not.
IS_DEBUG = False

#Define a boolean flag, if the flag is set(it is equal to true), then run the test. Otherwise do not run it.
IS_TEST = False

def read_district_file():
    """
    This function reads an MahalleVerileri.xlsx .
    It takes none argument.
    This function returns six variable:
        i)   names_of_district : List of NUMBER_OF_DISTRICT length which consists of district names like ["YAKUPLU" , ..]
        ii)  x_coordinates     : List of NUMBER_OF_DISTRICT length which consists of x_coordinates of centers of districts
        iii) y_coordinates     : List of NUMBER_OF_DISTRICT length which consists of y_coordinates of centers of districts
        iv)  from_district     : List of NUMBER_OF_DISTRICT * NUMBER_OF_DISTRICT length which consists of ids of from_district
        v)   to_district       : List of NUMBER_OF_DISTRICT * NUMBER_OF_DISTRICT length which consists of ids of to_district
        vi)  distances         : List of NUMBER_OF_DISTRICT * NUMBER_OF_DISTRICT length which consists of distances between from_district and to_district
    """

    # WORKS TO BE DONE: If the file is not there an exception should be raise as well

    #Read the excel file into df, since we have two different worksheets parse the excel file into two different worksheets
    all_data = pd.ExcelFile("MahalleVerileri.xlsx")
    worksheet_1 = all_data.parse('Mahalle Listesi')
    worksheet_2 = all_data.parse('Uzaklıklar')

    #Get the columns into columns
    columns_1 = worksheet_1.columns
    columns_2 = worksheet_2.columns

    #It is easier to work with list objects,so cast them to list objects.
    columns_1 = list(columns_1)
    columns_2 = list(columns_2)

    if IS_DEBUG == True:
        print("The columns in the first worksheet are: " , columns_1)
        print("The columns in the second workshett are: " , columns_2)

    #Read all the x_coordinates and y_coordinates
    names_of_district = worksheet_1['MAHALLE']
    x_coordinates = worksheet_1['X'].values
    y_coordinates = worksheet_1['Y'].values

    #Read all the from , to , distance
    from_district = worksheet_2['From']
    to_district = worksheet_2['To']
    distances = worksheet_2['Distance(m)']

    if IS_DEBUG == True:
        print("Length of from_district is: " , len(from_district))
        print("Length of to_district is: " , len(to_district))
        print("Length of distances is: " , len(distances))
        print("Length of the X coordinates is: " , len(x_coordinates))
        print("Length of the Y coordinates is: " , len(y_coordinates))

    return names_of_district , x_coordinates , y_coordinates , from_district , to_district , distances

def read_risk():
    """
    This function reads risks from "MahalleVerileri.xlsx" without spending any time.
    It takes no argument.
    It returns 1 variable:
        i) risks : A list , which contains direct risks of districts
    """
    all_data = pd.ExcelFile("MahalleVerileri.xlsx")
    worksheet_1 = all_data.parse('Mahalle Listesi')

    columns_1 = worksheet_1.columns
    columns_1 = list(columns_1)

    names = worksheet_1['MAHALLE']
    risks = worksheet_1['Risk Kodu']

    return risks

def read_appropriate_pairs(filename):
    """
    This function reads appropriate_pairs excel file and returns appropriate_pairs as a list of lists
    It takes 1 argument:
        i)  filename      : A string , which is filename of excel file
    It returns 2 variables:
        i)  from_district : A list , which consists of ids of from_district
        ii) to_district   : A list , which consists of ids of to_district
    """
    #Get the full_path using current_directory
    current_directory = util.get_current_directory()
    full_path = current_directory + "/Appropriate_Pairs/" + filename

    all_data = pd.ExcelFile(full_path)
    worksheet = all_data.parse('Sheet1')

    #Get the columns into columns
    columns = worksheet.columns

    #It is easier to work with list objects,so cast them to list objects.
    columns = list(columns)

    from_district = worksheet['From_District']
    to_district = worksheet['To_District']

    return from_district , to_district

def read_binary_txt(filename):
    """
    This function reads solution txt which consist of NUMBER_OF_DISTRICT binary values in line 1
    It takes 1 argument:
        filename : A string , which is the name of the txt file
    It returns 1 variable:
        solution_array : A list , which consist of NUMBER_OF_DISTRICT binary values
    """
    current_directory = util.get_current_directory()
    full_path = current_directory + "/Solutions/" + filename

    #Open the file and read the content of it into the variable "content"
    file = open(full_path , 'r')
    content = file.read()

    #Get rid of \n at the at of the content
    content = content.strip()

    #Collect all the elements in array
    solution_array = []
    for element in content:
        if element != ' ':
            solution_array.append(element)

    #Make the elements integer and win the war.
    for i in range(len(solution_array)):
        solution_array[i] = int(solution_array[i])

    return solution_array

def read_query_file(filename):
    """
    This function read a query file.
    It takes 1 argument:
        i) filename : A string , name of the excel file to read
    It returns 3 variables:
        i)   from_district : A list which consists of ids of from_district
        ii)  to_district   : A list which consists of ids of to_district
        iii) duration      : A list which consists of travel time between from_district and to_district such as "8 mins"
    """
    #Get the full path using current directory
    current_directory = util.get_current_directory()
    full_path = current_directory + "/Data_Points/" + filename

    #Open excel file
    d_excel_file = pd.ExcelFile(full_path)
    worksheet = d_excel_file.parse('Sheet1' , header = None)

    #Initialize the variables
    from_district = []
    to_district = []
    duration = []

    #Fill the variables usign excel data
    for i in range(len(worksheet)):
        from_district.append(worksheet.iloc[i , 0])
        to_district.append(worksheet.iloc[i , 1])
        duration.append(worksheet.iloc[i , 2])

    return from_district , to_district , duration

def combine_queries(length_of_appropriate_pairs):
    """
    This function reads all the cleaned query files, then it combines them in an array which consists of len(appropriate_pairs) lists each of which
    consists of 60 data points
    It takes no argument.
    It returns 1 variable:
        combined_data_points : A list of lists , whose length is len(appropriate_pairs) , each element list has length 60
    """

    #Get the full path using current_directory
    current_directory = util.get_current_directory()
    full_path = current_directory + "/New_Data_Points"

    #Initialize the variables
    combined_data_points = []
    for i in range(length_of_appropriate_pairs):
        combined_data_points.append([])

    #Iterate over all excel queries and add the data points accordingly
    for filename in os.listdir(full_path):
        if filename.endswith(".xlsx") and filename[0] == 'w':
            d_excel_file = pd.ExcelFile(full_path + "/" + filename)
            worksheet_1 = d_excel_file.parse('Sheet1' , header = None)
            for i in range(len(worksheet_1)):
                if worksheet_1.iloc[i,2] != 0 :
                    combined_data_points[i].append(worksheet_1.iloc[i,2])
        else:
            print("You are not a excel file dute.")

    return combined_data_points

def read_new_district_names(filename):
    """
    This function gives new_district_names
    """

    current_directory = util.get_current_directory()
    full_path = current_directory + "/Coords/" + filename

    all_data = pd.ExcelFile(full_path)
    worksheet_1 = all_data.parse('Sheet1')

    #Get the columns into columns
    columns_1 = worksheet_1.columns

    #It is easier to work with list objects,so cast them to list objects.
    columns_1 = list(columns_1)

    if IS_DEBUG == True:
        print("The columns in the first worksheet are: " , columns_1)
        print("The columns in the second workshett are: " , columns_2)

    #Read all the x_coordinates and y_coordinates
    old_district_names = worksheet_1['AD'].values

    #Get rid of empty districts
    new_district_names = []
    for i in range(len(old_district_names)):
        if type(old_district_names[i]) == type(" "):
            new_district_names.append(old_district_names[i])

    return new_district_names

def polygon_coords(filename):
    """
    This function reads x-y data of polygon coordinates and return it
    """

    #Get full_path using current_directory
    current_directory = util.get_current_directory()
    full_path = current_directory + "\Coords/" + filename


    all_data = pd.ExcelFile(full_path)
    worksheet_1 = all_data.parse('Sheet1')

    #Get the columns into columns
    columns_1 = worksheet_1.columns

    #It is easier to work with list objects,so cast them to list objects.
    columns_1 = list(columns_1)

    id_district = worksheet_1['shapeid'].values
    x_district = worksheet_1['x'].values
    y_district = worksheet_1['y'].values

    #Initialize variables
    lat = []
    longs = []

    for i in range(util.VIS_NUMBER_OF_DISTRICT):
        lat.append([])
        longs.append([])

    for i in range(len(x_district)):
        if pd.isna(x_district[i]) != True and pd.isna(y_district[i]) != True and pd.isna(id_district[i]) != True :
            while x_district[i] > 100 :
                x_district[i] /= 10

            while y_district[i] > 100 :
                y_district[i] /= 10

            lat[int(id_district[i]/10)].append(y_district[i])
            longs[int(id_district[i]/10)].append(x_district[i])

    return lat,longs

def read_distribution():
    """
    This function reads distribution file and returns name_of_distribution and parameters_of_distribution
    It takes no arguments.
    It returns 2 variables:
        i) name_of_distribution        : A list , which consists of names of distributions
        ii) parameters_of_distribution : A list , which consists of parameters of distributions
    """
    #Initialize variables
    name_of_distribution = []
    parameters_of_distribution = []

    four_parameter_dists = ["beta" , "johnsonsb" , "johnsonsu"]
    three_parameter_dists = ["gamma" , "weibull_min" , "weibull_max" , "triang"]
    two_parameter_dists = ["expon" , "norm" , "uniform"]


    d_excel_file = pd.ExcelFile("distribution_fit.xlsx")
    worksheet = d_excel_file.parse('Sheet1' , header = None)
    for i in range(len(worksheet)):
        parameters_of_distribution.append([])
        current_name = worksheet.iloc[i,0]
        name_of_distribution.append(current_name)
        if current_name in four_parameter_dists :
            upper_index = 5
        elif current_name in three_parameter_dists :
            upper_index = 4
        elif current_name in two_parameter_dists :
            upper_index = 3
        for k in range(1,upper_index):
            parameters_of_distribution[i].append(worksheet.iloc[i , k])

    return name_of_distribution , parameters_of_distribution

def read_availability_matrix(filename):
    """
    This function reads filename.xlsx and returns availability matrix.
    """

    #Get full path using current_directory
    current_directory = util.get_current_directory()
    full_path = current_directory + "/Availability_Matrix/" + filename

    #Open excel file to write
    excel_file = pd.ExcelFile(full_path)
    worksheet = excel_file.parse('Sheet1' , header = None)

    #Initialize availability_matrix
    availability_matrix = []

    for i in range(len(worksheet)):
        availability_matrix.append([])
        for k in range(util.NUMBER_OF_DISTRICT) :
            availability_matrix[i].append(worksheet.iloc[i][k])

    return availability_matrix

def read_cloud_solution(filename):
    """
    This function reads solution of the optimization problem which is solved by cplex_cloud
    """
    current_directory = util.get_current_directory()
    full_path = current_directory + "/Solutions/" + filename

    solution_file = open(full_path , 'r')
    content = solution_file.read()

    is_solution_start = False
    is_solution_end = False
    solution_array = []

    for i in range(len(content)) :
        if content[i : i + 5] == "y = [" :
            is_solution_start = True
        if is_solution_start == True and is_solution_end == False :
            if 48 <= ord(content[i]) <= 49 :
                solution_array.append(int(content[i]))

        if is_solution_start == True and content[i] == "]" :
            is_solution_end = True

    return solution_array

def read_selected_solution(filename):
    """
    This function reads solution of the optimization problem which is solved by cplex_cloud
    """

    solution_file = open(filename , 'r')
    content = solution_file.read()

    is_solution_start = False
    is_solution_end = False
    solution_array = []

    for i in range(len(content)) :
        if content[i : i + 5] == "y = [" :
            is_solution_start = True
        if is_solution_start == True and is_solution_end == False :
            if 48 <= ord(content[i]) <= 49 :
                solution_array.append(int(content[i]))

        if is_solution_start == True and content[i] == "]" :
            is_solution_end = True

    return solution_array

def read_generated_numbers():
    """
    This function reads generated_numbers and returns them as a 33000 * 100 matrix directly
    It takes no argument.
    """
    file = open("generated_random_numbers.txt" , 'r')
    content = file.read()

    names_of_district , x_coordinates , y_coordinates , from_districts , to_districts , distances = read_district_file()
    appropriate_pairs = util.generate_appropriate_pairs(from_districts , to_districts , distances , 7000)

    scenarios = []
    for i in range(len(appropriate_pairs)):
        scenarios.append([])

    in_index = 0
    out_index = 0
    temp = ""
    for char in content :
        if 48 <= ord(char) <= 57:
            temp += char
        elif temp != "":
            temp = int(temp)
            scenarios[out_index].append(temp)
            in_index += 1
            if in_index == 100:
                out_index += 1
                in_index = 0
            temp = ""

    return scenarios

def read_new_district_xy():
    """
    This function reads new x and y coordinates of centers of new districts
    It takes no arguments.
    It returns 2 variables:
        i)  new_x_coordinates : A list , which contains x coordinates of centers of new districts
        ii) new_y_coordinates : A list , which contains x coordinates of centers of new districts

    """
    all_data = pd.ExcelFile("Yeni_MahalleVerileri.xlsx")
    worksheet = all_data.parse('Sheet1')

    columns = worksheet.columns
    columns = list(columns)

    #Read all the x_coordinates and y_coordinates
    new_x_coordinates = worksheet['X'].values
    new_y_coordinates = worksheet['Y'].values

    return  new_x_coordinates , new_y_coordinates

def test():
    """
    Tests the above function
    """

    from_district , to_district , distances = read_excel_file('MahalleVerileri.xlsx')
    pair_array = get_appropriate_pairs(from_district , to_district , distances , 10000)
    print("Length of pair_array is:" , len(pair_array))
if IS_TEST == True:
    test()

def run():
    """
    Run the application
    """
    name_of_distribution , parameters_of_distribution = read_distribution()
    for i in range(5):
        print(name_of_distribution[i] , parameters_of_distribution[i])
#run()
#read_generated_numbers()
