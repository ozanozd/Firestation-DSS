//set
int Num_Districts=...;
int facility_number=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;

//parameters
float a [from_range][to_range]=...; //availability matrix

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise.
dvar boolean covered[to_range]; // if district j is covered 1, 0 otherwise.

//Model
maximize sum (j in to_range)covered[j];

subject to {

forall (j in to_range) sum(i in from_range) a[i][j]*y[i] >= covered[j]; //selection of districts to be covered

sum (i in from_range) y[i] <= facility_number; //fixed number of facilities

}
