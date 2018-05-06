//set
int Num_Districts=...;
int facility_number=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;
range scenario=1..100;

//parameters
float a [from_range][to_range][scenario]=...; //availability matrix
float covered[to_range][scenario]=...;
//float t[from_range][to_range][scenario]=...; //travel time from district i to district j under the scenario k
//float d[scenario]=...; //threshold under the scenario k

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise
// dvar boolean a [from_range][to_range][scenario]; Can be used for other method

//Model
maximize sum (j in to_range, k in scenario)covered[j][k];

subject to {

forall (j in to_range, k in scenario) sum(i in from_range) a[i][j][k]*y[i] >= covered[j][k]; //Each district is covered

sum (i in from_range) y[i] <= facility_number; //fixed number of facilities

//forall[i in from_range, j in to_range, k in scenario) t[i][j][k]*a[i][j][k]<=d[k];

}
