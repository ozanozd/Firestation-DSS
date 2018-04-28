#General library imports
import pandas
import os
import xlsxwriter
import statistic as sta

#Define a boolean flag , if the flag is set(it is equal to true), then, all the prints for debugging will be performed. Otherwise they will not.
IS_DEBUG = False

#Define a boolean flag, if the flag is set(it is equal to true), then run the test. Otherwise do not run it.
IS_TEST = False

NUMBER_OF_DISTRICT = 975

def get_district_names(filename):
    """
    This functions gets names of districts and returns the list.
    """
    all_data = pandas.ExcelFile(filename)
    worksheet_1 = all_data.parse('Mahalle Listesi')
    columns_1 = worksheet_1.columns
    columns_1 = list(columns_1)
    name_of_districts = worksheet_1['MAHALLE']

    return name_of_districts

def get_x_y_coordinates(filename):
    """
    This function gets x,y coordinates of the district and returns both lists.
    """
    all_data = pandas.ExcelFile(filename)
    worksheet_1 = all_data.parse('Mahalle Listesi')
    columns_1 = worksheet_1.columns
    columns_1 = list(columns_1)
    x_coordinates = worksheet_1['X'].values
    y_coordinates = worksheet_1['Y'].values

    return x_coordinates , y_coordinates

def read_excel_file(filename) :
    """
    This function reads an excel file given by user.
    It takes one argument :
        i) filename(string): name of the file which consist of the data
    This function returns nothing
    """

    # WORKS TO BE DONE: If the file is not there an exception should be raise as well

    #Read the excel file into df, since we have two different worksheets parse the excel file into two different worksheets
    all_data = pandas.ExcelFile(filename)
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

    return from_district , to_district , distances

def get_appropriate_pairs(from_district , to_district , distances , threshold ):
    """
    This function using the above function and returns the appropriate pairs
    It takes 4 arguments:
        i)   from_district(list) : It contains all from_district id's
        ii)  to_district(list)   : It contains all to_district   id's
        iii) distances(list)     : It contains all the distances(m)
        iv)  threshold(integer)  : If the distance between two district is greater than threshold distance , do not ask the query.
    It returns all the pairs
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

def read_binary_txt(filename):
    """
    This function takes a txt file which consists of 867 binary values at the first line.This function reads this values into a list,
    then returns that list.
    """

    #Open the file and read the content of it into the variable "content"
    file = open(filename , 'r')
    content = file.read()

    #Get rid of \n at the at of the content
    content = content.strip()

    #Collect all the elements in array
    array = []
    for element in content:
        if element != ' ':
            array.append(element)

    #Make the elements integer
    for i in range(len(array)):
        array[i] = int(array[i])

    return array

def clean_rewrite_data(directory):
    """
    This function takes a string in the form = /folder_path . Then, it iterates over all the excel file in this folder and get rid of min in the entries.
    It writes the new datas in excel files as well.
    """
    filename_array = []

    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") and filename[0] == 'q':
            from_districts = []
            to_districts = []
            old_values = []
            new_values = []
            d_excel_file = pandas.ExcelFile(directory + "/" + filename)
            worksheet_1 = d_excel_file.parse('Sheet1' , header = None)
            for i in range(len(worksheet_1)):
                from_districts.append(worksheet_1.iloc[i , 0])
                to_districts.append(worksheet_1.iloc[i , 1])
                old_values.append(worksheet_1.iloc[i , 2])
            for  i in range(len(old_values)):
                new_values.append(old_values[i][:-5])
            new_filename = directory + "/" + "w" + filename[1:]
            write_new_data(new_filename , from_districts , to_districts , new_values)
        else:
            print("You are not a excel file dute.")

def write_new_data(filename , from_districts , to_districts , new_values) :
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    for i in range(len(new_values)):
        worksheet.write(i , 0 , from_districts[i])
        worksheet.write(i , 1 , to_districts[i])
        worksheet.write(i , 2 , new_values[i])

    workbook.close()

def get_detailed_array(directory):
    """
    Detailed function.Secret of allies success in WW2.
    """
    array_of_array = []
    for i in range(4):
        array_of_array.append([])
    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") and filename[0] == 'w':
            d_excel_file = pandas.ExcelFile(directory + "/" + filename)
            worksheet_1 = d_excel_file.parse('Sheet1' , header = None)
            for i in range(len(worksheet_1)):
                array_of_array[i].append(worksheet_1.iloc[i,2])

        else:
            print("You are not a excel file dute.")
    print(array_of_array)
    sta.fit_dist(list(array_of_array[0]))
    return array_of_array

def coord_read(filename):
    """
    This function reads the x-y data of polygon coordinates and return it as a list of lists.
    """
    all_data = pandas.ExcelFile(filename)
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

    print(new_district_names)

def polygon_coords(filename):
    """
    This function reads x-y data of polygon coordinates and return it
    """
    all_data = pandas.ExcelFile(filename)
    worksheet_1 = all_data.parse('Sheet1')

    #Get the columns into columns
    columns_1 = worksheet_1.columns

    #It is easier to work with list objects,so cast them to list objects.
    columns_1 = list(columns_1)

    id_district = worksheet_1['shapeid'].values
    x_district = worksheet_1['x'].values
    y_district = worksheet_1['y'].values

    lat = []
    longs = []

    for i in range(NUMBER_OF_DISTRICT):
        lat.append([])
        longs.append([])

    for i in range(len(x_district)):
        if pandas.isna(x_district[i]) != True and pandas.isna(y_district[i]) != True and pandas.isna(id_district[i]) != True :
            while x_district[i] > 100 :
                x_district[i] /= 10

            while y_district[i] > 100 :
                y_district[i] /= 10

            lat[int(id_district[i]/10)].append(x_district[i])
            longs[int(id_district[i]/10)].append(y_district[i])

    return lat,longs
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
    #clean_rewrite_data("C:/Users/Ywestes/Desktop/Can/SabanciUniv/Year 4/ENS 491/Fire Station Location Codes/Firestation-DSS/DenemeExcel")
    #read_binary_txt('solution.txt')
    #get_detailed_array("C:/Users/Ywestes/Desktop/Can/SabanciUniv/Year 4/ENS 491/Fire Station Location Codes/Firestation-DSS/DenemeExcel")
    #coord_read("temp-attributes.xlsx")
    polygon_coords("temp-nodes.xlsx")
#run()
