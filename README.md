A collection of algotihms, links and paper and (naive) implementation

# VRP Algorithms
## Still in progress

A collection of VRP algorithms.

The following is the overview algorithms based on [NEO](http://neo.lcc.uma.es/vrp/solution-methods/).

![Overview](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/Overview.png)

## Variants
* CVRP
* VRPTW

## Exact Algorithm
* [Branch and bound](https://github.com/4342315yc/VRP-Algorithms/tree/master/Exact)
* [Branch and cut](https://github.com/4342315yc/VRP-Algorithms/tree/master/Exact)

## Heuristic Algorithm
* **[Constructive heuristic](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive)**
  * Clarke and Wright savings algorithm
  * Matching Based
  * Multi-route Improvement Heuristic
    * Thompson and Psaraftis
    * Van Breedam
    * Kinderwater and Savelsbergh

* **[2-Phase heuristic](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase)**
  * Cluster-First, Route-Second Algorithms
    * Fisher and Jakimar
    * The Petal Algorithm
    * The Sweep Algorithm
    * Tailard
  * Route-First, Cluster-Second Algorithms
    * Beasley's Algorithm

## Meta Heuristic Algorithm
* Ant Algorithms
* Constraint Programming
* Deterministic Annealing
* Genetic Algorithms
* Simulated Annealing
* Tabu Search
  * Granular Tabu
  * The Adaptative Memory Procedure
  * Kelly and Xu
  
## Deep Learning / Reinforcement Learning Approaches

## Additional Resources
VRP [Slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

SP [Slides](http://www2.imm.dtu.dk/courses/02735/sppintro.pdf) by **Jesper Larsen**, which may be useful for understanding the petal algorithm.
