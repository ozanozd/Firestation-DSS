//set
int Num_Districts=...;
float c=...;//confidence level
int p=...; //number

//ranges
range from_range=1..Num_Districts;
range to_range= 1..Num_Districts;
range scenario=1..100;

//parameters
tuple Pairs {
int d1;
int d2;
int scenario;
};
setof(Pairs) assign = ...;

// Decision Variables
dvar boolean y[from_range]; //if there is a station to be opened, takes value 1 for an element of from_range, 0 otherwise
dvar boolean s[to_range][scenario]; // if the constraint can be satisfied 1, otherwise 0.
dvar boolean z[to_range]; // if district j is covered.

//Model
maximize sum (j in to_range)z[j];

subject to {

forall (j in to_range,k in scenario) sum(<i,j,k> in assign) y[i] >= s[j][k];

forall (j in to_range) sum(k in scenario) s[j][k] >= c*z[j];

sum (i in from_range) y[i]<=p;

}
