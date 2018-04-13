import numpy
from docplex.mp.model import Model

mdl = Model(name='firestations')

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