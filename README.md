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

Here is a survey on the combinatorial optimization, which is a very general topic: [Machine Learning for Combinatorial Optimization:
a Methodological Tour d’Horizon](https://arxiv.org/pdf/1811.06128.pdf) by Yoshua Bengio, Andrea Lodi, and Antoine Prouvost

The following is a collection of some modern approaches on combinatorial problems mainly focusing on TSP/VRP.

[Pointer Network](https://arxiv.org/pdf/1506.03134.pdf) by Oriol Vinyals, Meire Fortunato and Navdeep Jaitly is specillay designed for the combinatorial optimization. In this paper, the autohers proposed a new neural nextwork called pointer network which outputs a permutation of the input. However, authors trained their model in a supervised way, which make use of heuristic to get the label. The disadvantage of this is that the labels(optimal solutinos) are hard to acquire when the size of the problem is too large. Meanwhile. the quality of the model is tied to the supervised label. If the labels are not good enough, the model is not able to get better solution.

[Neural Combinatorial Optimization with Reinforcement Learning](https://arxiv.org/pdf/1611.09940.pdf) by Irwan Bello, Hieu Pham, Quoc V. Le, Mohammad Norouzi, Samy Bengio. The authors made use of reinfoecement learning based on actor-critic

NIPS paper [Reinforcement Learning for Solving the Vehicle Routing Problem](https://arxiv.org/abs/1802.04240)

ICLR Paper of 2019 [Attention, Learn to Sovle Routing Problem](https://openreview.net/pdf?id=ByxBFsRqYm) is a recent paper proposed based on attention to solve the similar problem.

[Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem](https://arxiv.org/pdf/1911.09539.pdf) by Andre Hottung and Kevin Tierney. The authors apply DL to LNS (NLNS) and train the model based on different destroy operators and let the model learn the complex repair operator. The authors have shoen their method outperformed the two models mentioned above in batch search.

[Learning-Based Iterative Method for Solving Vehicle Routing Problems](https://openreview.net/pdf?id=BJe1334YDH), which is still under review now.

[Learning to Perform Local Rewriting for Combinatorial Optimization](https://arxiv.org/pdf/1810.00337.pdf) by Xinyun Chen and Yuandong Tian

[Learning Combinatorial Optimization Algorithms over Graphs](https://arxiv.org/pdf/1704.01665.pdf) by Hanjun Dai, Elias B. Khalil, Yuyu Zhang, Bistra Dilkina, Le Song.

[Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP](https://arxiv.org/pdf/1809.02721.pdf) by Marcelo Prates, Pedro H. C. Avelar, Henrique Lemos, Luis C. Lamb and Moshe Y. Vardi

[An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem](https://arxiv.org/pdf/1906.01227.pdf) by Chaitanya K. Joshi, Thomas Laurent and  Xavier Bresson.

## Additional Resources
VRP [Slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

SP [Slides](http://www2.imm.dtu.dk/courses/02735/sppintro.pdf) by **Jesper Larsen**, which may be useful for understanding the petal algorithm.

Intro to reinforcement learning: [Lil's log](https://lilianweng.github.io/lil-log/tag/reinforcement-learning)

David Silver's reinforcement learning [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) in UCL 

pgrouting [Github repo](https://github.com/pgRouting/pgrouting/wiki/VRP-Algorithms)

[Slides](https://imada.sdu.dk/~marco/Teaching/Fall2008/DM87/Slides/dm87-lec19-2x2.pdf) of some aspects of VRP.

There are 3 Github repos on TSP, which are taken from the appendix of the paper [Pointer Network](https://arxiv.org/pdf/1506.03134.pdf).
[1](https://github.com/dmishin/tsp-solver), [2](https://github.com/samlbest/traveling-salesman), [3](https://github.com/beckysag/traveling-salesman).

[LKH3 Solver](http://akira.ruc.dk/~keld/research/LKH-3/LKH-3_REPORT.pdf), which is one of powerful solvers that can be used for many variants of TSP and VRP (and applied to large size).
