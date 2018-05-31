#General library imports
import numpy
from docplex.mp.model import Model
from docloud.job import JobClient

#Inside project imports
import write_file as writer

CPLEX_BASE_URL = "https://api-oaas.docloud.ibmcloud.com/job_manager/rest/v1/"
CPLEX_API_KEY = "api_dac7438b-d31e-4038-9910-019cc0f29d2a"

#######################################################################################################
# NOTE : There is no connection check for client. If the connection fails then , program will crash..
#######################################################################################################

def run(choice , threshold , confidence_interval , facility_number , min_threshold):
    """
    This solves the corresponding optimization problem to cplex cloud.
    It takes 5 parameters:
        i) choice                : An integer , (1-5) which represents the optimization model choice of the user
        ii) threshold(m)         : An integer , which represents the maximum possible distance between two districts which are counted as appropriate_pairs , meter
        iii) confidence_interval : An integer , (0-100) which represents the confidence level of the stochastic model
        iv) facility_number      : An integer , (0 - NUMBER_OF_DISTRICT) which represents the maximum fire station number for maximum coverage models
        v) min_threshold(min)    : An integer , which represents the maximum traveling time between two districts in terms of minutes.

    It returns nothing but it creates a .txt file that contains the solution of the corresponding optimization problem.
    """
    #Create a clinet
    client = JobClient(CPLEX_BASE_URL, CPLEX_API_KEY)

    # Choice == 1 , base model
    if choice == 1:
        resp = client.execute(input = [ "Mod_Files/BaseModel.mod",
                                "Mod_Files/BaseModel_" + str(threshold) + ".dat"],
                                output = "Solutions/BaseModel_Sol_" + str(threshold) + ".txt")

        return "Solutions/BaseModel_Sol_" + str(threshold) + ".txt"

    # Choice == 2 , max_coverage model
    if choice == 2:
        resp = client.execute(input = [ "Mod_Files/MultiCoverage.mod",
                                "Mod_Files/MultiCoverage_" + str(threshold) + ".dat"],
                                output = "Solutions/MultiCoverage_Sol_" + str(threshold) + ".txt")

        return "Solutions/MultiCoverage_Sol_" + str(threshold) + ".txt"

    # Choice == 3 , max coverage
    if choice == 3:

        resp = client.execute(input = [ "Mod_Files/MaxCoverage.mod",
                                "Mod_Files/MaxCoverage_" + str(threshold) + "_" + str(facility_number) + ".dat"],
                                output = "Solutions/MaxCoverage_Sol_" + str(threshold) + "_" + str(facility_number) +  ".txt")

        return "Solutions/MaxCoverage_Sol_" + str(threshold) + "_" + str(facility_number) +  ".txt"

    # Choice == 4 , stochastic_coverage
    if choice == 4:
        resp = client.execute(input = [ "Mod_Files/StochasticCoverage.mod",
                                "Mod_Files/Stochastic_Coverage_" + str(min_threshold) + "_" + str(confidence_interval) + ".dat"],
                                output = "Solutions/Stochastic_Coverage_Sol_" + str(min_threshold) + "_" + str(confidence_interval) + ".txt")

        return "Solutions/Stochastic_Coverage_Sol_" + str(min_threshold) + "_" + str(confidence_interval) + ".txt"

    # Choice == 5 , stochastic max coverage
    if choice == 5:
        resp = client.execute(input = [ "Mod_Files/MaxCoverage.mod",
                                "Mod_Files/Stochastic_MaxCoverage_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".dat"],
                                output = "Solutions/Stochastic_MaxCoverage_Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".txt")

        return "Solutions/Stochastic_MaxCoverage_Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".txt"
