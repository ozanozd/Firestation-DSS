/*********************************************
 * OPL 12.6.2.0 Model
 * Author: ozanozdemir
 * Creation Date: 02 Þub 2018 at 11:56:08
 *********************************************/

//set
int Num_Districts=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;

//parameters
float a [from_range][to_range]=...; //availability matrix
float f_cost[from_range]=...; //station cost matrix

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise

//Model
minimize sum (i in from_range)f_cost[i]*y[i];

subject to {

forall (j in to_range) sum(i in from_range) a[i][j]*y[i] >= 1; //Each district is covered

}