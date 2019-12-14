Exact algorithms try all the possible solutions to the problem and then find out the best one.

## Branch and bound

Branch and bound algorithm divides the problems into subproblems and solve each of them individually. Once a better solution is found, it replaces the current solution with the better one. 

If a branch is found to have no solutions then its discarded.

## Branch and cut

Similar to branch and bound but with pruning. If we know the best feasible solution from a branch is no better than the current solution, then we prune the subproblem and continue to next one.

## Paper
**M.L.Fisher** [Optimal Solution of Vehicle Routing Problems Using Minimum K-trees](http://users.mai.liu.se/torla64/MAI0127/Fisher1994.pdf),  1994.
