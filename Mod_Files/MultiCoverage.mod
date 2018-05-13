//set
int Num_Districts=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;
range risk_category=1..4;

//parameters
float a [from_range][to_range]=...; //availability matrix
float f_cost[from_range]=...; //station cost matrix
float r[to_range][risk_category]=...; // The risk indicator matrix
float n[risk_category]=...; //number of stations that a district in risk category k need.

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise

//Model
minimize sum (i in from_range)f_cost[i]*y[i];

subject to {

forall (j in to_range,k in risk_category) sum(i in from_range) a[i][j]*y[i] >= r[j][k]*n[k]; //Each district is covered

}
