## Clarke and Wright savings algorithm
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
## Multi-route Improvement Heuristic
  * Thompson and Psaraftis
  * Van Breedam
  * Kinderwater and Savelsbergh
