Exact algorithms try all the possible solutions to the problem and then find out the best one.

## Branch and bound

Branch and bound algorithm divides the problems into subproblems and solve each of them individually. Once a better solution is found, it replaces the current solution with the better one. 

If a branch is found to have no solutions then its discarded.

## Branch and cut

Similar to branch and bound but with pruning. If we know the best feasible solution from a branch is no better than the current solution, then we prune the subproblem and continue to next one.

## Resoureces
**M.L.Fisher**. [Optimal Solution of Vehicle Routing Problems Using Minimum K-trees](http://users.mai.liu.se/torla64/MAI0127/Fisher1994.pdf),  1994.

**P. Toth, and D. Vigo**. [Models, relaxations and exact approaches for the capacitated vehicle routing problem](http://www-dimat.unipv.it/~gualandi/famo2conti/papers/routing_models.pdf). 2000.

**P. Toth, and D. Vigo**. [Branch-and-bound algorithms for the capacitated VRP](https://www.jstor.org/stable/171544?seq=1#metadata_info_tab_contents). 2001.

**U. Blasum, and W. Hochstattler**. [Application of the Branch and Cut Method to the Vehicle Routing Problem](https://pdfs.semanticscholar.org/f2b6/7aab794949152bc73d3f606e4ad36f1d6390.pdf). 2002.

**R. Fukasawa1, J. Lysgaard2, M. Poggi de Aragao, M. Reis3, E. Uchoa4, and R. F. Werneck**. [Robust Branch-and-Cut-and-Price for the Capacitated Vehicle Routing Problem](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.90.394&rep=rep1&type=pdf) as well as this [slides](https://pdfs.semanticscholar.org/6b1a/e2c40e0e9eef4c367416053b78d2d7ebaf0d.pdf).

**AN Letchford1, J Lysgaard2 and RW Eglese1**. [A new branch-and-cut algorithm for the capacitated vehicle routing problem](https://www.lancaster.ac.uk/staff/letchfoa/articles/2007-covrp.pdf) and
[Slides](https://symposia.cirrelt.ca/system/documents/000/000/112/Lysgaard_original.pdf?1441306917).
