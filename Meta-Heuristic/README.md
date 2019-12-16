# Ant Algorithms

Accoridng to  [Bullnheimer et al. 1997](http://neo.lcc.uma.es/vrp/wp-content/data/articles/bullnheimer97AS.pdf), the ant system consists of two phases: construction of vehicle routes and trail update.

Wikipedia provides a elegant formulation of AS algorithm in *Algorithm and formulae* section.

* **Construction (Edge selection)**

The probabiliy of selecting an edge is calculated as following: 

![ant]()

Where

![e](https://latex.codecogs.com/png.latex?\dpi{120}&space;\fn_cm&space;\fn_cm&space;{\Omega&space;=&space;\left&space;\lbrace&space;v_{j}&space;\in&space;V&space;:&space;v_{j}&space;\;&space;\text{is&space;feasible&space;to&space;be&space;visited}&space;\right&space;\rbrace&space;\bigcup&space;\left&space;\lbrace&space;v_{0}&space;\right&space;\rbrace})

The *attractiveness*  ![eta](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\eta_{ij}) of the move, as computed by some heuristic indicating the a priori desirability of that move.

The *trail level* ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\tau_{ij}) of the move, indicating how proficient it has been in the past to make that particular move(typically ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;\frac{1}{d_{ij}}), where ![tau](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;d_{ij}) is the distance between two states). The trail level represents a posteriori indication of the desirability of that move.

* **Trail Update (Pheromone update)**

![1](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;{&space;\tau_{ij}^{new}&space;=&space;\rho\tau_{ij}^{old}&space;&plus;&space;\sum_{\mu&space;=&space;1}^{\sigma-1}\Delta\tau_{ij}^{\mu}&space;&plus;&space;\sigma&space;\Delta&space;\tau_{ij}^{*}&space;})

Or according to Wikipedia: 

![2](https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\fn_cm&space;{&space;\tau_{ij}=&space;(1-\rho)\tau_{ij}&space;&plus;&space;\sum_{k}\Delta&space;\tau_{ij}^k&space;})

where ![3](https://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;\fn_cm&space;\rho) in the first equation is the *trail persistance* and ![4](https://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;\fn_cm&space;\rho) in the second equation is the *pheromone evaporation coefficient*.

And ![](), where **Q** is a constant.

# Constraint Programming


# Deterministic Annealing


# Genetic Algorithms


# Simulated Annealing


# Tabu Search

## Granular Tabu

## The Adaptative Memory Procedure

## Kelly and Xu
