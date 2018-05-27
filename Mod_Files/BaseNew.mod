//set
int Num_Districts=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;

//parameters
float f_cost[from_range]=...; //station cost matrix

tuple Pairs {
int d1;
int d2;
};
setof(Pairs) assign = ...;
int a[assign] = ...;

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise

//Model
minimize sum (i in from_range)f_cost[i]*y[i];

subject to {

forall (j in to_range) sum(<i,j> in assign) a[<i,j>]*y[i] >= 1; //Each district is covered

}