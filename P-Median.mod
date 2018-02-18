//set
int Num_Districts=...;
int facility_number=...;

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;

//parameters
float a [from_range][to_range]=...; //availability matrix
float time[from_range][to_range]=...;
float x[from_range][to_range]=...;

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise

//Model
minimize sum (i in to_range) sum (j in to_range) time[i][j]*x[i][j];

subject to {

forall (j in to_range) sum(i in from_range) x[i][j] == 1;

forall (i in from_range) 
forall (j in to_range) x[i][j] <= y[i];

sum (i in from_range) y[i] <= facility_number; //fixed number of facilities

}
