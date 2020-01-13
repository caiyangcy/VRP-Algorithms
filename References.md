# Reference Used in this repo

* A general overview on VRP algorithms: [Classical and modern heuristics for the vehicle routing problem](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1475-3995.2000.tb00200.x)

* [NEO](http://neo.lcc.uma.es/vrp/) website on VRP

* VRP [Slides](http://www.discovery.dist.unige.it/didattica/LS/VRP.pdf) by **Massimo Paolucci**.

* SP [Slides](http://www2.imm.dtu.dk/courses/02735/sppintro.pdf) by **Jesper Larsen**.

* Intro to reinforcement learning: [Lil's log](https://lilianweng.github.io/lil-log/tag/reinforcement-learning)

* David Silver's reinforcement learning [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) in UCL 

* pgrouting [Github repo](https://github.com/pgRouting/pgrouting/wiki/VRP-Algorithms)

* VRP [Slides](https://imada.sdu.dk/~marco/Teaching/Fall2008/DM87/Slides/dm87-lec19-2x2.pdf).

* There are 3 Github repos on TSP, which are taken from the appendix of the paper [Pointer Network](https://arxiv.org/pdf/1506.03134.pdf).
[1](https://github.com/dmishin/tsp-solver), [2](https://github.com/samlbest/traveling-salesman), [3](https://github.com/beckysag/traveling-salesman).

* [LKH3 Solver](http://akira.ruc.dk/~keld/research/LKH-3/LKH-3_REPORT.pdf), which is one of powerful solvers that can be used for many variants of TSP and VRP (and applied to large size).

* TSP [Concorde](http://www.math.uwaterloo.ca/tsp/concorde.html) solver


## Heuristic


## Meta-Heuristic


## Deep Learning / Reinforcement Learning Approaches

Here is a survey on the combinatorial optimization, which is a very general topic: [Machine Learning for Combinatorial Optimization:
a Methodological Tour d’Horizon](https://arxiv.org/pdf/1811.06128.pdf) by Yoshua Bengio, Andrea Lodi, and Antoine Prouvost.

The following is a collection of some modern approaches on combinatorial problems mainly focusing on TSP/VRP. It turns out these DL/RL models are rather limited to solve VRP of small to medium size while solutions to larger size of VRP still depend on meta-heuristic.

* [Pointer Network](https://arxiv.org/pdf/1506.03134.pdf) by Oriol Vinyals, Meire Fortunato and Navdeep Jaitly. PN is specillay designed for the combinatorial optimization. In this paper, the autohers proposed a new neural network called pointer network which outputs a permutation of the input. However, authors trained their model in a supervised way, which makes use of heuristic to get the label. The disadvantage of this is that the labels(optimal solutinos) are hard to acquire when the size of the problem is too large. Meanwhile. the quality of the model is tied to the supervised label. If the labels are not good enough, the model is not able to get better solution.

* [Neural Combinatorial Optimization with Reinforcement Learning](https://arxiv.org/pdf/1611.09940.pdf) by Irwan Bello, Hieu Pham, Quoc V. Le, Mohammad Norouzi, Samy Bengio. The authors made use of reinfoecement learning based on actor-critic training along with different search strategies: sampling and active search.

* [Reinforcement Learning for Solving the Vehicle Routing Problem](https://arxiv.org/abs/1802.04240) by Mohammadreza Nazari, Afshin Oroojlooy, Martin Takac and Lawrence V. Snyder. The authors think the RNN used in original PN is not necessary since the order of the input sequence does not matter. Hence Therefore, the authors simply leave out the encoder RNN and directly use the embedded inputs instead of the RNN hidden states. On capacitated VRP, the approach outperforms classical heuristics and Google’s OR-Tools on medium-sized instances in solution quality with comparable computation time (after training). The authors also showed their approach can be applied to stochastic VRP and even more general problem of combinatorial problem.

* [Attention, Learn to Sovle Routing Problem](https://openreview.net/pdf?id=ByxBFsRqYm) by Wouter Kool, Herke van Hoof and Max Welling. The authors propose a model based on attention layers with benefits over the PN and they show how to train the model using REINFORCE with a simple baseline based on a deterministic greedy rollout. This model has outperformed a wide range of baselines and get highly near-optimal results.

* [Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem](https://arxiv.org/pdf/1911.09539.pdf) by Andre Hottung and Kevin Tierney. The authors apply DL to LNS (NLNS) and train the model based on different destroy operators and let the model learn the complex repair operator. The authors have shoen their method outperformed the two models mentioned above in batch search.

* [Learning-Based Iterative Method for Solving Vehicle Routing Problems](https://openreview.net/pdf?id=BJe1334YDH), which is still under review now.

* [Learning to Perform Local Rewriting for Combinatorial Optimization](https://arxiv.org/pdf/1810.00337.pdf) by Xinyun Chen and Yuandong Tian

* [Learning Combinatorial Optimization Algorithms over Graphs](https://arxiv.org/pdf/1704.01665.pdf) by Hanjun Dai, Elias B. Khalil, Yuyu Zhang, Bistra Dilkina, Le Song.

* [Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP](https://arxiv.org/pdf/1809.02721.pdf) by Marcelo Prates, Pedro H. C. Avelar, Henrique Lemos, Luis C. Lamb and Moshe Y. Vardi

* [An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem](https://arxiv.org/pdf/1906.01227.pdf) by Chaitanya K. Joshi, Thomas Laurent and Xavier Bresson.
