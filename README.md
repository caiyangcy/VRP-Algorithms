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

Note that the following hyperlinks in sub-sections may not work

* **[Constructive heuristic](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive)**
  * [Clarke and Wright savings algorithm](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/#clarke-and-wright-savings-algorithm)
  * [Matching Based](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/#matching-based)
  * [Multi-route Improvement Heuristic](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/#multi-route-improvement-heuristic)
    * [Thompson and Psaraftis](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/#thompson-and-psaraftic)
    * [Van Breedam](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/#van-breedam)
    * [Kinderwater and Savelsbergh](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/Constructive/kinderwater-and-savesbergh)

* **[2-Phase heuristic](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase)**
  * [Cluster-First, Route-Second Algorithms](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#cluster-first-route-second-algorithms)
    * [Fisher and Jakimar](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#fisher-and-jakimar)
    * [The Petal Algorithm](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#the-petal-algorithm)
    * [The Sweep Algorithm](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#the-sweep-algorithm)
    * Tailard
  * [Route-First, Cluster-Second Algorithms](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#route-first-cluster-second-algorithms)
    * [Beasley's Algorithm](https://github.com/4342315yc/VRP-Algorithms/tree/master/Heuristic/2-Phase/#beasleys-algorithm)

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
