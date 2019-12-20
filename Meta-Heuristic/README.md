A lot of the following are taken from [NEO](http://neo.lcc.uma.es/vrp/solution-methods/) and Wikipedia.

# Ant Algorithms

Accoridng to  [Bullnheimer et al. 1997](http://neo.lcc.uma.es/vrp/wp-content/data/articles/bullnheimer97AS.pdf), the ant system consists of two phases: construction of vehicle routes and trail update.

[Wikipedia](https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms) provides a elegant formulation of AS algorithm in *Algorithm and formulae* section.

* **Construction (Edge selection)**

The probabiliy of selecting an edge is calculated as following: 

![ant](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/AS_prob.png)

Where

![e](https://latex.codecogs.com/png.latex?\dpi{120}&space;\fn_cm&space;\fn_cm&space;{\Omega&space;=&space;\left&space;\lbrace&space;v_{j}&space;\in&space;V&space;:&space;v_{j}&space;\;&space;\text{is&space;feasible&space;to&space;be&space;visited}&space;\right&space;\rbrace&space;\bigcup&space;\left&space;\lbrace&space;v_{0}&space;\right&space;\rbrace})

The *attractiveness*  ![eta](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\eta_{ij}) of the move, as computed by some heuristic indicating the a priori desirability of that move.

The *trail level* ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\tau_{ij}) of the move, indicating how proficient it has been in the past to make that particular move(typically ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\frac{1}{d_{ij}}), where ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;d_{ij}) is the distance between two states). The trail level represents a posteriori indication of the desirability of that move.

* **Trail Update (Pheromone update)**

![1](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;{&space;\tau_{ij}^{new}&space;=&space;\rho\tau_{ij}^{old}&space;&plus;&space;\sum_{\mu&space;=&space;1}^{\sigma-1}\Delta\tau_{ij}^{\mu}&space;&plus;&space;\sigma&space;\Delta&space;\tau_{ij}^{*}&space;})

Or according to Wikipedia: 

![2](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;{&space;\tau_{ij}=&space;(1-\rho)\tau_{ij}&space;&plus;&space;\sum_{k}\Delta&space;\tau_{ij}^k&space;})

where ![3](https://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;\fn_cm&space;\rho) in the first equation is the *trail persistance* and ![4](https://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;\fn_cm&space;\rho) in the second equation is the *pheromone evaporation coefficient*.

And 

![4](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/AS_delta.png), 

where **Q** is a constant.

# Constraint Programming

[Python library for CP](https://pypi.org/project/python-constraint/). And [Wikipedia](https://en.wikipedia.org/wiki/Constraint_programming#Constraint_programming_libraries_for_general-purpose_programming_languages) provides a list of languages that support CP.

Problems are expressed in terms of variables, domains for those variables and constraints between the variables. The problems are then solved using complete search techniques such as depth-first search (for satisfaction) and branch and bound (for optimisation).

The typical methods for CP are *chronological backtracking* and *constraint propagation*. 

*Backtracking* is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 

*Local consistency* conditions are properties of constraint satisfaction problems related to the consistency of subsets of variables or constraints. They can be used to reduce the search space and make the problem easier to solve. Various kinds of local consistency conditions are leveraged, including *node consistency*, *arc consistency*, and *path consistency*. Every *local consistency* condition can be enforced by a transformation that changes the problem without changing its solutions. Such a transformation is called *constraint propagation*.

* Core Constraints

1. Time

2. Capacity

* Side constraints

Solutions to CP problems are usually found using complete methods such as depth-first search and branch and bound. However, for routing problems of practical size, complete search methods cannot produce solutions in a short and reliable time period. By contrast, iterative improvement methods have proved very successful in this regard. Iterative improvement methods operate by changing small parts of the solution, for instance moving a visit from one route to another. This type of operation involves retracting previous decisions and making new ones. In contrast to depth-first search, retraction can be done in any order, not simply in the opposite order the decisions were made. In general the overhead of implementing this type of non-chronological retraction mechanism in CP frameworks is very high.

To overcome this problem, the CP system is only used to check the validity of solutions and determine the values of constrained variables, not to search for solutions. The search is performed by an iterative improvement procedure. When the procedure needs to check the validity of a potential solution, it is handed to the CP system. As a part of checking, constraint propagation using all constraints still takes place. This adds value to the constraint check, as the iterative improvement method can then take advantage of the reduced domains to speed up search by performing fast legality checks.

If the propagation mechanism removes all values from any variable, then there cannot be a solution in this subtree and the search backtracks making a different decision at the backtrack point.

# Deterministic Annealing

Deterministic Annealing operates in a way that is similar to SA, except that a deterministic rule is used for the acceptance of a move. Two standard implementations of this technique are threshold accepting [Dueck and Scheurer 1990] and record to record travel [Dueck 1993].

At iteration t of a threshold accepting algorithm, solution ![10](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;(x_{i+1})) is accepted if ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x_{i&plus;1})&space;\le&space;f(x_{i})&plus;&space;\theta_{1}) here ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_1) is a user controlled parameter. In record-to-record travel a record is the best solution ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x^{*}) encountered during the search. At iteration t, solution ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x_{i+1}) is accepted if ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x_{i&plus;1})&space;\le&space;\theta_{2}f(x_{i})), where ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_2) is a user controlled parameter slightly larger than ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_1).

# Genetic Algorithms

Inspired by the natural selection, genetic algorithm is used a meta-heeuritic algorithm being used a lot to generate high-quality solutions based on bio-inspired operations such as mutation, crossover and selection.

The evolution usually starts from a population of randomly generated individuals, and is an iterative process, with the population in each iteration called a generation. In each generation, the *fitness* of every individual in the population is evaluated; the *fitness* is usually the value of the objective function in the optimization problem being solved. 

A picture illustrating of GA. (solutions are aften represented as a string of bits, which are problem specific):

![](https://miro.medium.com/max/1600/1*BYDJpa6M2rzWNSurvspf8Q.png)

In general, there are some common phases for GA:

1. **Initialization**. A *papulation* in GA refers to a set of candidate solutions(called *individual*, encoded as *chromosomes*) and the size of it is depending on the problem. The initial population is generated randomly, allowing the entire range of possible solutions (the search space). Occasionally, the solutions may be "seeded" in areas where optimal solutions are likely to be found.

2. **Selection**. The process consist of randomly choosing two parent individuals from the population for mating purposes. The probability of selecting a population member is generally proportional to its fitness in order to emphasize genetic quality while maintaining genetic diversity. (Fitness can also be considered as a measure of profit, utility or goodness to be maximized while exploring the solution space.). Diversity is ensured by selecting parents with less fitness value.

3. **Genetic operators** This process refers to generate a new generation through genetic operators: crossover(AKA recombination) and mutation.

    * **Crossover**. The process makes use of genes of selected parents to produce offspring that will form the next generation. Although reproduction methods that are based on the use of two parents are more "biology inspired", some research suggests that more than two "parents" generate higher quality chromosomes.
  
    * **Mutation**. It consists of randomly modifying some gene(s) of a single individual at a time to further explore the solution space and ensure, or preserve, genetic diversity. The occurrence of mutation is generally associated with a low probability.

**Heuristic**. In addition to the main operators above, other heuristics may be employed to make the calculation faster or more robust. The speciation heuristic penalizes crossover between candidate solutions that are too similar; this encourages population diversity and helps prevent premature convergence to a less optimal solution.

There are usually multiple stopping ctriteria such as the number of iterations is reached, the whole population converges to a homogeneous system with similar individuals or an optimal solution is found.

For solving VRP with GAs, it is usual to represent each individual by just one chromosome, which is a chain of integers, each of them representing a customer or a vehicle. So that each vehicle identifier represents in the chromosome a separator between two different routes, and a string of customer identifiers represents the sequence of deliveries that must cover a vehicle during its route. In the figure below we can see a representation of a possible solution for VRP with 10 customers and 4 vehicles. Each route begins and end at the depot (it will be assigned the number 0). If we find in a solution two vehicle identifiers not separated by any customer identifier, we will understand that the route is empty and, therefore, it will not be necessary to use all the vehicles available.

![](https://latex.codecogs.com/png.latex?\inline&space;\dpi{120}&space;\fn_cm&space;\large&space;\underbrace{4-5-2}_{route1}-11-\underbrace{10-3-1}_{route2}-13-\underbrace{7-8-9}_{route3}-12-\underbrace{6}_{route4})

A typical fitness function used for solving VRP with GA is ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f_{eval}(x)&space;=&space;f_{max}-f(x)) where ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;{f(x)&space;=&space;totaldistance(x)&space;&plus;&space;\lambda&space;overcapacity(x)&space;&plus;&space;\mu&space;overtime(x)}) is the *unfitness* value.

The **overcapacity** and **overtime** functions are acting as a penaly term and they measured the amount of capacity and time that is over the maximum. If no violations on the capacity and time, the function will simply return the total distance and hence the fitness value is better.

There are still other functions can be used as the fitness value function such as the reciprocal of the total travelled distance

# Simulated Annealing

Simulated Annealing (SA) is a stochastic relaxation technique, which has its origin in statistical mechanics. It is based on an analogy from the annealing process of solids, where a solid is heated to a high temperature and gradually cooled in order for it to crystallize in a low energy configuration. SA can be seen as one way of trying to allow the basic dynamics of hill-climbing to also be able to escape local optima of poor solution quality. SA guides the original local search method in the following way. The solution **S’** is accepted as the new current solution if ![5](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\Delta&space;\leq&space;0), where ![7](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\Delta&space;=&space;f(x)-f(x_i)). To allow the search to escape a local optimum, moves that increase the objective function value are accepted with a probability ![8](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;e^{-\Delta/T}) if $![9](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\Delta&space;>&space;0), where *T* is a parameter called the “temperature”. The value of *T* varies from a relatively large value to a small value close to zero. These values are controlled by a cooling schedule, which specifies the initial, and temperature values at each stage of the algorithm.

At iteration **t** of Simulated Annealing, a solution **x** is drawn randomly in ![10](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;N(x_{i})). If ![11](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x)&space;\le&space;f(x_{i})), then ![12](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x_{i+1}) is set equal to **x**; otherwise 

![13](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;{x_{i&plus;1}=\begin{cases}&space;x&space;&&space;\text{with&space;probability&space;}p_{i}\\\\&space;x_{i}&space;&&space;\text{with&space;probability&space;}1-p_{i}&space;\end{cases}})

where ![12](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;p_{i}) is usually a decreasing function of **t** and of ![12](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x)-f(x_i)). It's usually set to be ![8](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;e^{-\Delta/T})

The stopping criteria is usually divided into three cases: 

1. The value ![13](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f^{*}) of the incumbent ![14](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x^{*}) has not decreased by at least ![15](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\pi_1) % for at least ![16](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;k_1) consecutive cycle of **T** iterations;

2. The number of accepted moves has been less than ![16](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\pi_{2}\%) % of **T** for ![17](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;k_2) consecutive cycles of **T** iterations;

3. ![19](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;k_3) of **T** iterations have been executed.

Also an example of annealing on CVRP (I forgot which paper this image was taken from):

![6](https://github.com/4342315yc/VRP-Algorithms/blob/master/Images/cvrp_annealing.png)

# Tabu Search

Tabu search is a metaheuristic search method employing local search methods used for mathematical optimization.

Local (neighborhood) searches take a potential solution to a problem and check its immediate neighbors (that is, solutions that are similar except for very few minor details) in the hope of finding an improved solution. Local search methods have a tendency to become stuck in suboptimal regions or on plateaus where many solutions are equally fit.

Tabu search enhances the performance of local search by relaxing its basic rule. First, at each step worsening moves can be accepted if no improving move is available (like when the search is stuck at a strict local minimum). In addition, prohibitions (henceforth the term tabu) are introduced to discourage the search from coming back to previously-visited solutions.

The implementation of tabu search uses memory structures that describe the visited solutions or user-provided sets of rules. If a potential solution has been previously visited within a certain short-term period or if it has violated a rule, it is marked as "tabu" (forbidden) so that the algorithm does not consider that possibility repeatedly.

The initial solution is typically created with some cheapest insertion heuristic. After creating an initial solution, an attempt is made to improve it using local search with one or more neighborhood structures and a best-accept strategy. Most of the neighborhoods used are well known and were previously introduced in the context of various construction and improvement heuristics.

## Granular Tabu

It turns out the longer the distance is, the less likely it is to belong to the optimal solution. Hence by defining *granularity threshold*, several unpromising solutions will never be considered by the search process. The authors proposed ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;\nu&space;=&space;\beta&space;\bar{c}), where ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;\beta) is a sparsification parametetr typically chosen from interval [1.0, 2.0] (the percentage of remaining edges in the graph tends to be in the 10% – 20%) and ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;\bar{c}) is the averaged edge length of a solution obtained by a fast heuristic. The value of ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;\beta) is dynamically adjusted whenever the incumbent has not improved for a set number of iterations, and periodically decreased to its initial value. Neighbor solutions are obtained by performing a limited number of edge exchanges within the same route or between two routes.

The authors proposed a procedure capable of examining all potential exchanges in ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;O(|E(\nu)|)), where ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;E(\nu)&space;=&space;\{(i,j)&space;\in&space;E&space;:&space;c_{ij}&space;\le&space;\nu\}&space;\bigcup&space;I) and ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\large&space;I) is the set od important edges such as the inevitable edges between customers and deopts or the edged that are very likely to show up in the best edges.

## The Adaptative Memory Procedure

An adaptative memory is a pool of good solutions that is dynamically updated throughout the search process. Periodically, some elements of these solutions are extracted from the pool and combined differently to produce new good solutions. When selecting these routes, care must be taken to avoid including the same customer twice in a solution. This restriction means that the selection process will often terminate with a partial solution that will have to be completed using a construction heuristic. In the example depicted in the figure below, extracting routes A, D and H from a memory of two solutions results in a partial solution. Rochat and Taillard have shown that the application of an adaptative memory procedure can enhance a search strategy. This has enabled them to obtain two new best solutions on the 14 standard VRP benchmark instances.


## Kelly and Xu

In this case, [Kelly and Xu 1996] considered swaps of vertices between two routes, a global repositioning of some vertices into other routes, and local routes improvements. The global repositioning strategy solves a network flow model to optimally relocate given numbers of vertices into different routes. Approximations are developed to compute the ejection and insertion costs, taking vehicle capacity into account. Route optimizations are performed by means of 3-opt exchanges. The algorithm is governed by several parameters which are dynamically adjusted through the search. A pool of best solutions is memorized and periodically used to reinitiate the search with new parameter values. Overall, this algorithm produced several best known solutions on benchmark instances, but it is fair to say that it is not as effective as some other TS implementations. It tends to require a meaty computational effort and properly tuning its many parameters can be problematic.
