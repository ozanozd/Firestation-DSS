#General library imports
import numpy
from docplex.mp.model import Model
from docloud.job import JobClient

CPLEX_BASE_URL = "https://api-oaas.docloud.ibmcloud.com/job_manager/rest/v1/"
CPLEX_API_KEY = "api_df058b14-fb2d-4010-9cef-c92cfa379561"
#Inside project imports
import write_file as writer

def run(choice , threshold , confidence_interval , facility_number , min_threshold):
    client = JobClient(CPLEX_BASE_URL, CPLEX_API_KEY)

    if choice == 1:
        resp = client.execute(input = [ "Mod_Files/BaseModel.mod",
                                "Mod_Files/BaseModel_" + str(threshold) + ".dat"],
                                output = "Solutions/BaseModel_Sol_" + str(threshold) + ".txt")

        return "Solutions/BaseModel_Sol_" + str(threshold) + ".txt"

    if choice == 2:
        resp = client.execute(input = [ "Mod_Files/MultiCoverage.mod",
                                "Mod_Files/MultiCoverage_" + str(threshold) + ".dat"],
                                output = "Solutions/MultiCoverage_Sol_" + str(threshold) + ".txt")

        return "Solutions/MultiCoverage_Sol_" + str(threshold) + ".txt"
    if choice == 3:

        resp = client.execute(input = [ "Mod_Files/MaxCoverage.mod",
                                "Mod_Files/MaxCoverage_" + str(threshold) + "_" + str(facility_number) + ".dat"],
                                output = "Solutions/MaxCoverage_Sol_" + str(threshold) + "_" + str(facility_number) +  ".txt")

        return "Solutions/MaxCoverage_Sol_" + str(threshold) + "_" + str(facility_number) +  ".txt"

    if choice == 4:
        resp = client.execute(input = [ "Mod_Files/BaseModel.mod",
                                "Mod_Files/Stochastic_Coverage_" + str(min_threshold) + "_" + str(confidence_interval) + ".dat"],
                                output = "Solutions/Stochastic_Coverage_Sol_" + str(min_threshold) + "_" + str(confidence_interval) + ".txt")

        return "Solutions/Stochastic_Coverage_Sol_" + str(min_threshold) + "_" + str(confidence_interval) + ".txt"

    if choice == 5:
        resp = client.execute(input = [ "Mod_Files/MaxCoverage.mod",
                                "Mod_Files/Stochastic_MaxCoverage_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".dat"],
                                output = "Solutions/Stochastic_MaxCoverage_Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".txt")

        return "Solutions/Stochastic_MaxCoverage_Sol_" + str(min_threshold) + "_" + str(facility_number) + "_" + str(confidence_interval) + ".txt"
print("Sey oldu bisiy oldu baska bisiy oldu.")
