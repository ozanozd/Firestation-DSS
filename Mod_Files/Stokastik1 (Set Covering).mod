//set
int Num_Districts=...;
float C=...;//confidence level

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;
range scenario=1..100;

//parameters
float a [from_range][to_range][scenario]=...; //availability matrix
float f_cost[from_range]=...; //station cost matrix
//float t[from_range][to_range][scenario]=...; //travel time from district i to district j under the scenario k
//float d[scenario]=...; //threshold under the scenario k

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise
dvar boolean s[to_range][scenario]; // if the constraint can be satisfied 1, otherwise 0.
// dvar boolean a [from_range][to_range][scenario]; Can be used for other method

//Model
minimize sum (i in from_range)f_cost[i]*y[i];

subject to {

forall (j in to_range,k in scenario) sum(i in from_range) a[i][j][k]*y[i] >= s[j][k]; 

forall (j in to_range) sum(k in scenario) s[j][k] >= C;

//forall[i in from_range, j in to_range, k in scenario) t[i][j][k]*a[i][j][k]<=d[k];
}
