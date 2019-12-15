# Cluster-First, Route-Second Algorithms

## Fisher and Jakimar

This algorithm refers to solve a *GA(generalized assignment)* problem.

*Step 1*: Seed selection. Select a seed ![](https://latex.codecogs.com/gif.latex?j_k) in V for each cluster k=1,..,K.

*Step 2*: Allocation of customers to seed. Compute the cost ![](https://latex.codecogs.com/gif.latex?c_{ik}) of allocating customer *i* to *k* as the cost of inserting *i* in the route ![](https://latex.codecogs.com/gif.latex?0-j_k-0). ![](https://latex.codecogs.com/gif.latex?c_{ik}=min(c_{0i}&plus;c_{ij_k}&plus;c_{j_k0},&space;c_{0j_k}&plus;c_{j_ki}&plus;c_{i0})-&space;(c_{0j_k}&plus;c_{j_k0}))

*Step 3*:  Generailzed assignment. Sovle a GA problem with costs ![](https://latex.codecogs.com/gif.latex?c_{ik}), weights for customer ![](https://latex.codecogs.com/gif.latex?d_i), and vehicle capacity *Q*.

*Step 4*: TSP solution. Solve a TSP for each cluster found.

The following is taken from page 69 of the [slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**:

![sweep_0](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/fisher_demo.png)

## The Sweep Algorithm

Imagine a ray centered at the depot. By rotating the ray, the customers can be divided into multiple clusters. By performing a TSP algorithm on each cluster we can form a solution in the end.

The following is two pictures taken from page 68 of the [slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

![sweep_0](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/sweep_demo_0.png)

![sweep_1](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/sweep_demo_1.png)

## The Petal Algorithm

**Massimo Paolucci**'s slides really did a good job on explaining the algorithms. So I'm going to refer to his slides here again.  


## Tailard

## Location based heuristic
  
# Route-First, Cluster-Second Algorithms

## Beasley's Algorithm

Phase 1: Routing

By relaxing the constraint on capacity(infinite capacity), the problem is converted to a TSP.

Phase 2: Clustering

Cut the TSP solutions into sub-routes that satisfy the capacity constraints

Here, again, an example taken from the slides.




