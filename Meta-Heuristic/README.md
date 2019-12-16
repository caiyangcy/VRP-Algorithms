A lot of the following are taken from [NEO](http://neo.lcc.uma.es/vrp/solution-methods/)

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


# Deterministic Annealing

Deterministic Annealing operates in a way that is similar to SA, except that a deterministic rule is used for the acceptance of a move. Two standard implementations of this technique are threshold accepting [Dueck and Scheurer 1990] and record to record travel [Dueck 1993].

At iteration t of a threshold accepting algorithm, solution ![10](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;(x_{i+1})) is accepted if ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x_{i&plus;1})&space;\le&space;f(x_{i})&plus;&space;\theta_{1}) here ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_1) is a user controlled parameter. In record-to-record travel a record is the best solution ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x^{*}) encountered during the search. At iteration t, solution ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;x_{i+1}) is accepted if ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;f(x_{i&plus;1})&space;\le&space;\theta_{2}f(x_{i})), where ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_2) is a user controlled parameter slightly larger than ![](https://latex.codecogs.com/png.latex?\inline&space;\fn_cm&space;\theta_1).

# Genetic Algorithms


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

## Granular Tabu

## The Adaptative Memory Procedure

## Kelly and Xu
