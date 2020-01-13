# Reference Used in this repo

A general overview on VRP algorithms: [Classical and modern heuristics for the vehicle routing problem](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1475-3995.2000.tb00200.x)

VRP [Slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

SP [Slides](http://www2.imm.dtu.dk/courses/02735/sppintro.pdf) by **Jesper Larsen**, which may be useful for understanding the petal algorithm.

Intro to reinforcement learning: [Lil's log](https://lilianweng.github.io/lil-log/tag/reinforcement-learning)

David Silver's reinforcement learning [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) in UCL 

pgrouting [Github repo](https://github.com/pgRouting/pgrouting/wiki/VRP-Algorithms)

[Slides](https://imada.sdu.dk/~marco/Teaching/Fall2008/DM87/Slides/dm87-lec19-2x2.pdf) of some aspects of VRP.

There are 3 Github repos on TSP, which are taken from the appendix of the paper [Pointer Network](https://arxiv.org/pdf/1506.03134.pdf).
[1](https://github.com/dmishin/tsp-solver), [2](https://github.com/samlbest/traveling-salesman), [3](https://github.com/beckysag/traveling-salesman).

[LKH3 Solver](http://akira.ruc.dk/~keld/research/LKH-3/LKH-3_REPORT.pdf), which is one of powerful solvers that can be used for many variants of TSP and VRP (and applied to large size).

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
