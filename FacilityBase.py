
from __future__ import print_function

from math import fabs
import sys

import cplex
from cplex.exceptions import CplexSolverError
from inputdata import read_dat_file



# Read in data file. If no file name is given on the command line
# we use a default file name. The data we read is
# availability_matrix   -- a list/array of binary values which indicates 
#                         if that facility available to meet the reach that district
# fixedcost  -- a list/array of facility fixed cost

	
# need to assign corresponding data to the following parameters
availability_matrix, fixedcost

# number of districts
num_districts = len(fixedcost)

# decision variable
assignvars = []

def setupproblem(c):
	c.objective.set_sense(c.objective.sense.maximize)

    # assignment variables: assignvars[i][j] = 1 if district j is covered by
    #                                            district i
    
	c.variables.add(names=assignvars, lb=[0] * len(assignvars), 
					ub=[1] * len(assignvars),
					types=["B"] * len(assignvars))
	
	for i in range(num_districts):
		thevars = [assignvars[i]]
		for j in range(num_districts):
			availability_matrix[i][j]