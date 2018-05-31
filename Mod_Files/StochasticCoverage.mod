//set
int Num_Districts=...;
float c=...;//confidence level

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;
range scenario=1..100;

//parameters
float a [from_range][to_range][scenario]=...; //availability matrix
float f_cost[from_range]=...; //station cost matrix

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise
dvar boolean beta[to_range][scenario]; // if the constraint can be satisfied 1, otherwise 0.
dvar boolean ozans[scenario]; // one of the most detailed dvar ever created by a programmer from su...
// dvar boolean a [from_range][to_range][scenario]; Can be used for other method

//Model
minimize sum (i in from_range)f_cost[i]*y[i];

subject to {
forall (j in from_range ,  k in scenario) sum(i in to_range) (y[i] * a[i][j][k] == 1) >= ozans[k];
sum (k in scenario) ozans[k] >= c;

//forall (j in from_range) sum(k in scenario) (sum(i in to_range) (y[i]*a[i][j][k]==1)>=1) >= c;
}
