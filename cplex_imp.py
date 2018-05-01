#General library imports
import numpy
from docplex.mp.model import Model
from docloud.job import JobClient

CPLEX_BASE_URL = "https://api-oaas.docloud.ibmcloud.com/job_manager/rest/v1/"
CPLEX_API_KEY = "api_df058b14-fb2d-4010-9cef-c92cfa379561"
#Inside project imports
import write_file as writer

current_directory = writer.reader.util.get_current_directory()
full_path = current_directory + "/Mode_Files/" + "BaseModel.mod"
#context.solver.docloud.url = CPLEX_BASE_URL
#context.solver.docloud.key = CPLEX_API_KEY

client = JobClient(CPLEX_BASE_URL, CPLEX_API_KEY)
resp = client.execute(input = [ "availability_matrix_7000.xlsx",
                                "Mod_Files/BaseModel.mod" ],
                          output = "haaaaati.txt")
"""
mdl = Model(name="Haydi_Bakalim" , context = )


Num_Districts = 7;
a = [[1,1,0,1,0,0,1],
[1,1,0,0,1,1,1],
[0,0,1,1,1,1,0],
[0,0,1,1,0,0,1],
[0,1,1,0,1,1,0],
[0,1,1,0,1,1,0],
[1,1,0,1,0,0,1]]

f_cost = [1000,800,1200,1100,900,900,1100]

y = {d: mdl.binary_var(name="y"+str(d)) for d in range(1,Num_Districts+1)}

for j in range(1,Num_Districts+1):
    z=mdl.sum(y[i]*a[i-1][j-1] for i in range(1,Num_Districts+1))
    mdl.add_constraint(1<=mdl.sum(a[i-1][j-1]*y[i] for i in range(1,Num_Districts+1)))

mdl.minimize(mdl.sum(y[i]*f_cost[i-1] for i in range(1,Num_Districts+1)))

if not mdl.solve():
    print("*** Problem has no solution")
else:
    mdl.print_solution()
"""
