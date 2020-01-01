# Common Terminologies and Algorithms

Here is a list of collection of terminologies and algorithms which are common seen in those VRP paper for quick check.

## Intensification/Diversification

**diversification** = **exploration** (found a new  best solutions in the population).

**intensification** = **exploitation** (use the latest best solution to find a new oneslike metaheuristics who are guided by the best solution).

## Generalized Insertion (GENI)

Paper: [A GENERALIZED INSERTION HEURISTIC FOR THE TRAVELING SALESMAN PROBLEM WITH TIME WINDOWS](https://pubsonline.informs.org/doi/pdf/10.1287/opre.46.3.330). MICHEL GENDREAU, ALAIN HERTZ, GILBERT LAPORTE and MIHNEA STAN. 

Paper: [New Insertion and Postoptimization Procedures for the Traveling Salesman Problem (https://www.researchgate.net/publication/221704722_New_Insertion_and_Postoptimization_Procedures_for_the_Traveling_Salesman_Problem)

GENI is a technique used for for inter-route local search. It includes two types of insertion. The demos of Type I insertion and Type II insertion are as follows(taken from the two paper above).

![](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/GENI_types.png)

![](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/Type_I_GENI.png)
![](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/Type_II_GENI.png)

Refer to the second paper for the details of the GENI algorithm.

## Unstringing and Stringing (US)

US is post-optimization algorithm which consists of removing a vertex from a feasible solution and reinserting it back. Stringing procedure is similar to GENI and Unstringing is just reverse. The demos of Type I Unstringing and Type II Unstringing are as follow (taken from the second paper):

Refer to the second paper for the detail of the US algorithm.

## Nearest Insertion

Wikipedia provides the algorithm for NN insertion. The basic idea is always pick up the nearest uninserted point to the current route(tp any node the current route) and insert into the route. Repeat until all points are inserted. 

Also refer to this [post](https://cs.stackexchange.com/a/88935).

## Large Neighbourhood Search (LNS)

Paper: [Using Constraint Programming and Local Search Methods to Solve Vehicle Routing Problems](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.67.8526&rep=rep1&type=pdf). Paul Shaw. April 1998.

Taken from the paper: 

*LNS makes moves like local search, but uses a tree-based search with constraint propagation to evaluate the cost and legality of the move. As a “heavyweight” technique such as constraint programming is used to evaluate the move, many less moves per second can be evaluated than is normally the case for local search. However, these moves can be more powerful, moving the search further at each step. When such far reaching moves are possible there are normally many more of them available than would be the case if the moves were very localized: hence the name Large Neighbourhood Search.*

## Limited Discrepancy Search (LDS)

Paper: [Limited Discrepancy Search](https://pdfs.semanticscholar.org/efa5/6b710ff3c6d8b2666971d07c311eeb6c5b40.pdf?_ga=2.176917669.1045710749.1577795756-1357849254.1576571462). Willia m D. Harvey and Matthew L. Ginsberg. 

## λ-interchange

Inter-route. It's defined by Osman (Metastrategy simulated annealing and tabu search for combinatorial optimization problems). The basic idea is swap the two subsets of two different route, whose size is bouded by λ.

## k-opt

Intra-route. Swap k non-adjacent edges. 2-opt and 3-opt are the mostly common one. Possible changes: O(n^k)

## Or opt

Inter-route. Relocate 1, 2, or 3 consecutive vertices. Possisble changes for 2 consecutive: O(n^2). 

## Farthest Inesrtion

Refer to this [website](https://users.cs.cf.ac.uk/C.L.Mumford/howard/FarthestInsertion.html)

# First Improving (FI)

Accept the first improved solution.

# Best Improving (BI)

Accept the best improved solution.
