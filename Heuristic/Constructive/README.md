## Clarke and Wright savings algorithm

**Paper** : G. Clarke and J.W.Wright [Scheduling of vehicles from a central depot to a number of delivery points](https://www.jstor.org/stable/167703?seq=1#metadata_info_tab_contents) 1964

In this algorithm, *saving* is defined to be the distance saved by merging two seperate routes, i.e. ![](https://latex.codecogs.com/gif.latex?{s_{ij}=c_{i0}&plus;c_{0j}-c_{ij}}), where ![](https://latex.codecogs.com/gif.latex?c_{i0},&space;c_{0j},&space;c_{ij}) is defined as the distance between the depot with customer *i*, as the distance between the depot with customer *j*, and as the distance between customer *i* and customer *j*.

By ordering the savings in a non-inceasing order and merging those routes with largest savings first, this algorithm could manage to find a near-optimal solution to the problem.

There two versions of this algorithm, sequential and parallel respectively and both of them require calculating the savings first. After that, the sequential algorithm picks up one route and repeat merging other feasible routes to the current one until there is no more feasible routes and then consider the next route and reapply the same procedure. While the parallel algorithm starts from the largest savings and determine if there are two routes that can be feasibly merged. Here a feasible merge refers to the total demand of customers of two merged routes does not exceed the maximum capacity of the vehicle.

More, taken from [NEO](http://neo.lcc.uma.es/vrp/solution-methods/heuristics/savings-algorithms/) website:

Step 1. Savings computation
  * Compute the savings ![](https://latex.codecogs.com/gif.latex?{s_{ij}=c_{i0}&plus;c_{0j}-c_{ij}}) for ![](https://latex.codecogs.com/gif.latex?i,j&space;=&space;1,...,n) and ![](https://latex.codecogs.com/gif.latex?i&space;\neq&space;j)
  * Create *n* vehicle routes ![](https://latex.codecogs.com/gif.latex?(0,i,0)) for ![](https://latex.codecogs.com/gif.latex?i&space;=&space;1,...,n)
  * Order the savings in a non increasing fashion.

Step 2. Best feasible merge (Parallel version)
Starting from the top of the savings list, execute the following:
  * Given a saving ![](https://latex.codecogs.com/gif.latex?s_{ij}), determine whether there exist two routes that can feasibility be merged:
    * One starting with ![](https://latex.codecogs.com/gif.latex?(0,j))
    * One ending with ![](https://latex.codecogs.com/gif.latex?(i,0))
  * Combine these two routes by deleting ![](https://latex.codecogs.com/gif.latex?(0,j)) and ![](https://latex.codecogs.com/gif.latex?(i,0)) and introducing ![](https://latex.codecogs.com/gif.latex?(i,j)).

Step 2. Route Extension (Sequential version)
  * Consider in turn each route ![](https://latex.codecogs.com/gif.latex?(0,i,..,j,0))
  * Determine the first saving ![](https://latex.codecogs.com/gif.latex?s_{ki}) or ![](https://latex.codecogs.com/gif.latex?s_{jl}) that can feasibly be used to merge the current route with another route ending with ![](https://latex.codecogs.com/gif.latex?(k,0)) or starting with ![](https://latex.codecogs.com/gif.latex?(0,l)).
  * Implement the merge and repeat this operation to the current route.
  * If not feasible merge exists, consider the next route and reapply the same operations.
  * Stop when not route merge is feasible.

## Matching Based

**Paper**: 
Maybe a relevant paper on SBPP. A.Shafahi, Z. Wang, A. Haghani [A matching-based heuristic algorithm for school bus routing problems](https://arxiv.org/ftp/arxiv/papers/1807/1807.05311.pdf).

K. Altinkemer, and B.Gavish. “Parallel Savings Based Heuristic for the Delivery Problem”. 1991.

M. Desrochers, and T. W. Verhoog. “A Matching Based Savings Algorithm for the Vehicle Routing Problem”. 1989.

An modification to standard savings algorithm, where savings is calculated by ![](https://latex.codecogs.com/gif.latex?{s_{ij}=t(S_{i})&plus;t(S_{j})-t(S_{i}&space;\bigcup&space;S_{j})}). Here, ![](https://latex.codecogs.com/gif.latex?S_{k}) is the set containing all vertices from route *k* and ![](https://latex.codecogs.com/gif.latex?tS_{k}) is the TSP solution to the set

One variant involves approximating the TSP solution of each route instead of calculating the exact solution.

## Multi-route Improvement Heuristic

### Thompson and Psaraftis

The author describes a general “b-cyclic, k-transfer” scheme in which a circular permutation of b routes is considered and k customers from each route are shifted to the next route of the cyclic permutation. The authors show that applying specific sequences of b-cyclic, k-transfer exchanges (with b = 2 or b variable, and k = 1 or 2) yields interesting results. Due to the complexity of the cyclic transfer neighborhood search, it is performed heuristically.

Example of 3-cyclic-2-transfer:

![cyclic_demo](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/cyclic_transfer_demo.png)

The cyclic transfer operator. The basic idea is to transfer simultaneously the customers denoted by white circles in cyclical manner between the routes. More precisely here customers a and c in route 1, f and j in route 2 and o and p in route 4 are simultaneously transferred to routes 2, 4, and 1 respectively and route 3 remains untouched.

### Van Breedam

Van Breedam classifies the improvement operations as *string cross*, *string exchange*, *string relocation*, and *string mix*, which can all be viewed as special cases of 2-cyclic exchanges, and provides a computational analysis on a restricted number of test problems.

String Cross (SC): Two strings (or chains) of vertices are exchanged by crossing two edges of two different routes.

![SC_demo](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/van_0.png)

String Exchange (SE): Two strings of at most k vertices are exchanged between two routes.

![SE_demo](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/van_1.png)

String Relocation (SR): A string of at most k vertices is moved from one route to another, typically with k = 1 or 2.

![SR_demo](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/van_2.png)

String Mix (SM): The best move between SE and SR is selected.


### Kinderwater and Savelsbergh

Define similar operations and perform experiments mostly in the context of the VRP with time windows (VRPTW is not the main focus in this repo).


G. A. P. Kinderwater and M. W. P. Savelsbergh. [Vehicle Routing: Handling Edge Exchanges](https://pdfs.semanticscholar.org/e0a5/55b01d71f5ebdc653cf68b3ab8fc136ba47b.pdf). 1997.

P. M. Thompson and H. N. Psaraftis. [Cyclic Transfer Algorithms for the Multivehicle Routing and Scheduling Problems](https://www.jstor.org/stable/171656?seq=1#metadata_info_tab_contents). 1993.

A. Van Breedam. An Analysis of the Behavior of Heuristics for the Vehicle Routing Problem for a Selection of Problems with Vehicle-Related. 1994.
