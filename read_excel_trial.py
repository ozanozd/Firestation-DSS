import pandas

def read_excel_file(filename) :
    """
    This function reads an excel file given by user.
    It takes one argument :
        i) filename(string): name of the file which consist of the data
    This function returns nothing
    """

    #Read the excel file into df
    xls = pandas.ExcelFile(filename)
    df1 = xls.parse('Mahalle Listesi')
    df2 = xls.parse('Uzaklıklar')

    #Get the columns into columns
    columns_1 = df1.columns
    columns_2 = df2.columns
    list_columns_2 = list(columns_2)
    print("As a list, columns2 are: " , list_columns_2)
    print("Type of the columns is : " , type(columns_1))
    list_columns_1 = list(columns_1)
    print("As a list, columns are: " , list_columns_1)
    print("The columns in the files are: " , columns_1)

    #Read all the x_coordinates
    x_coordinates = df1['X'].values
    y_coordinates = df1['Y'].values

    #Read all the from , to , distance
    from_district = df2['From']
    to_district = df2['To']
    distances = df2['Distance(m)']
    print("Type of elements is:" , type(distances[1]))

    print("Length of from_district is:" , len(from_district))
    print("Length of to_district is:" , len(to_district))
    print("Length of distances is:" , len(distances))
    print("Length of the X coordinates is: " , len(x_coordinates))
    print("Length of the Y coordinates is: " , len(y_coordinates))
    
    return from_district , to_district , distances

    

def get_appropriate_pairs(from_district , to_district , distances , threshold ):
    """
    This function using the above function and returns the appropriate pairs
    It takes 3 arguments:
        i)   from_district(list) : It contains all from_district id's
        ii)  to_district(list)   : It contains all to_district   id's
        iii) distances(list)     : It contains all the distances(m)
    It returns all the pairs
    """

    pair_array = []
    #Iterate over all enties
    for i in range(len(distances)) :
        district_1 = from_district[i]
        district_2 = to_district[i]

        #We found an appropriate pair if the following if statement is satisfied
        if district_1 < district_2 and distances[i] <= threshold :
            pair_array.append([district_1 , district_2])


    return pair_array

def test():
    """
    Tests the above function
    """
    
    from_district , to_district , distances = read_excel_file('MahalleVerileri.xlsx')        
    pair_array = get_appropriate_pairs(from_district , to_district , distances , 10000)
    print("Length of pair_array is:" , len(pair_array))


