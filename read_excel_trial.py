import pandas

#Define a boolean flag , if the flag is set(it is equal to true), then, all the prints for debugging will be performed. Otherwise they will not.
IS_DEBUG = False

#Define a boolean flag, if the flag is set(it is equal to true), then run the test. Otherwise do not run it.
IS_TEST = False


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
        if distances[i] <= threshold :
            pair_array.append([district_1 , district_2])

    return pair_array

def test():
    """
    Tests the above function
    """

    from_district , to_district , distances = read_excel_file('MahalleVerileri.xlsx')
    pair_array = get_appropriate_pairs(from_district , to_district , distances , 10000)
    print("Length of pair_array is:" , len(pair_array))
if IS_TEST == True:
    test()
