A collection of algotihms, links and paper and (naive) implementation

# VRP Algorithms
## Still in progress

A collection of VRP algorithms.

The following is the overview algorithms based on [NEO](http://neo.lcc.uma.es/vrp/solution-methods/).

![Overview](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/Overview.png)

## Variants
* [CVRP](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#capacitated-vrpcvrp)
* [VRPTW](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#vrp-with-time-windowvrptw)
* [SVRP](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#stochastic-vrpsvrp)
* [VRPPPD](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#vrp-with-pick-up-and-deliveringvrppd)
* [VRPB](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#vrp-with-backhaulsvrpb)
* [SDVRP](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#stochastic-vrpsvrp)
* [MDVRP](https://github.com/4342315yc/VRP-Algorithms/blob/master/Variants/README.md#multiple-depot-vrpmdvrp)

## Exact Algorithms
* [Branch and bound](https://github.com/4342315yc/VRP-Algorithms/tree/master/Exact)
* [Branch and cut](https://github.com/4342315yc/VRP-Algorithms/tree/master/Exact)

## Heuristic Algorithms

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

## Meta Heuristic Algorithms
* [Ant Algorithms](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#ant-algorithms)
* [Constraint Programming](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#constraint-programming)
* [Deterministic Annealing](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#deterministic-annealing)
* [Genetic Algorithms](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#genetic-algorithms)
* [Simulated Annealing](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#simulated-annealing)
* [Tabu Search](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#tabu-search)
  * [Granular Tabu](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#granular-search)
  * [The Adaptative Memory Procedure](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#the-adaptative-memory-procedure)
  * [Kelly and Xu](https://github.com/4342315yc/VRP-Algorithms/tree/master/Meta-Heuristic#kelly-and-xu)
  
## Deep Learning / Reinforcement Learning Approaches

[Pointer Network](https://arxiv.org/pdf/1506.03134.pdf) is specillay designed for the combinatorial optimization.

[Neural Combinatorial Optimization with Reinforcement Learning](https://arxiv.org/pdf/1611.09940.pdf)

NIPS paper [Reinforcement Learning for Solving the Vehicle Routing Problem](https://arxiv.org/abs/1802.04240)

ICLR Paper of 2019 [Attention ! Learn to Sovle Routing Problem](https://openreview.net/pdf?id=ByxBFsRqYm) is a recent paper proposed based on attention to solve the similar problem.

## Additional Resources
VRP [Slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

SP [Slides](http://www2.imm.dtu.dk/courses/02735/sppintro.pdf) by **Jesper Larsen**, which may be useful for understanding the petal algorithm.

Intro to reinforcement learning: [Lil's log](https://lilianweng.github.io/lil-log/tag/reinforcement-learning)

David Silver's reinforcement learning [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) in UCL 

pgrouting [Github repo](https://github.com/pgRouting/pgrouting/wiki/VRP-Algorithms)

[Slides](https://imada.sdu.dk/~marco/Teaching/Fall2008/DM87/Slides/dm87-lec19-2x2.pdf) of some aspects of VRP.

There are 3 Github repos on TSP, which are taken from the appendix of the paper [Pointer Network](https://arxiv.org/pdf/1506.03134.pdf).
[1](https://github.com/dmishin/tsp-solver), [2](https://github.com/samlbest/traveling-salesman), [3](https://github.com/beckysag/traveling-salesman).
