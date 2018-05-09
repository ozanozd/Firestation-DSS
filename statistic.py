import write_file as writer
import scipy.stats as sta

DIST_NAMES =    [ 'beta' ,  'expon' , 'gamma' , 'johnsonsb' , 'johnsonsu' ,  'norm' , 'triang' ,  'uniform'                ,
                  'weibull_min' , 'weibull_max' ]
DISTRIBUTIONS = [ sta.beta ,  sta.expon , sta.gamma , sta.johnsonsb , sta.johnsonsu , sta.norm , sta.triang , sta.uniform ,
                  sta.weibull_min , sta.weibull_max , sta.wrapcauchy]

def find_best_fit(data):
    """
    This function find the best fitting distrubiton for given data.
    It takes 1 argument:
        i)  data                 : A list   , which contains floating points numbers
    It return 2 variables:
        i)  params               : A tuple  , which contains parameters of the best fitting distribution
        ii) name_of_distribution : A string , which is the name of the best fitting distribution
    """
    for i in range(len(data)):
        data[i] = float(data[i])
    #Initialize Variables
    p_values = []
    params = []
    for i in range(len(DIST_NAMES)):
        pars = DISTRIBUTIONS[i].fit(data)
        kstest_sta , p_val  = sta.kstest(data , DIST_NAMES[i] , pars)
        p_values.append(p_val)
        params.append(pars)

    temp_max = float('-inf')
    index = 0
    for i in range(len(p_values)):
        if p_values[i] > temp_max :
            temp_max = p_values[i]
            index = i

    return params[index] , DIST_NAMES[index]

def generate_random_number(dist_name , param):
    """
    This function generates one random number from the dist_name with param parameters
    """
    index = DIST_NAMES.index(dist_name)
    if len(param) == 2:
        arg1 = param[0]
        arg2 = param[1]
        return int(round(DISTRIBUTIONS[index].rvs(arg1 , arg2)))
    if len(param) == 3:
        arg1 = param[0]
        arg2 = param[1]
        arg3 = param[2]
        return int(round(DISTRIBUTIONS[index].rvs(arg1 , arg2 , arg3)))
    if len(param) == 4:
        arg1 = param[0]
        arg2 = param[1]
        arg3 = param[2]
        arg4 = param[3]
        return int(round(DISTRIBUTIONS[index].rvs(arg1 , arg2 , arg3 , arg4)))


def test():
    """
    """
    names_of_district , x_coordinates , y_coordinates , from_district , to_district , distances = writer.reader.read_district_file()
    print("Step1 Done")
    appropriate_pairs = writer.reader.util.get_appropriate_pairs(from_district , to_district , distances , 7000)
    print("Step2 Done")
    all_query_results = writer.reader.combine_queries(len(appropriate_pairs))
    print("Step3 Done")

    params = []
    dist_names = []
    for i in range(len(appropriate_pairs)) :
        if i % 100 == 0 :
            print("We finished" , i , "appropriate_pairs.")
        param , dist_name = find_best_fit(all_query_results[i])
        params.append(param)
        dist_names.append(dist_name)
    writer.write_distributions(dist_names , params)
    print("Sey oldu bisiy oldu baska bisiy oldu.")


def run():
    """
    This function takes all the queries corresponds the appropriate pairs then find the best fitting distribution for each pair in the appropriate_pairs.
    """
    fixed_cost = writer.reader.util.generate_fixed_cost_array()
    dist_names , parameters_of_distribution = writer.reader.read_distribution()
    random_numbers = []
    for i in range(len(dist_names)):
        if i % 1000 == 0 :
            print("We completed" , i , "tasks.")
        random_numbers.append([])
        for k in range(100):
            current_number = generate_random_number(dist_names[i] , parameters_of_distribution[i])
            max_iter = 0
            while 0 <= current_number <= 180 and max_iter != 5 :
                current_number = generate_random_number(dist_names[i] , parameters_of_distribution[i])
                max_iter += 1
            if current_number <= 0:
                random_numbers[i].append(15)
            elif current_number > 180:
                random_numbers[i].append(180)
            else :
                random_numbers[i].append(current_number)
    writer.write_generated_numbers(random_numbers , fixed_cost)
    print("Sey oldu bisiy oldu baska bisiy oldu")
#run()
