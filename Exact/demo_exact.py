'''
Implementation of some exact algorithms.
No optimisation yet.
CVRP
'''

import numpy as np
import matplotlib.pyplot as plt
import class_info as Exact
from matplotlib.animation import FuncAnimation


    
def plot_solutions():
    None
    
def plot_progress():
    None
    
def demo(ps=True, pp=False):
    
    if ps:
        print()
#        plot_solutions(solution)
    
    None
    
if __name__ == '__main__':
    
    depot = np.array([[0,0]])
#    customers = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
    customers = np.array([[1,1], [1,2], [-1,2]])
    demand = np.array([1,2,3,4])
    
    cvrp = Exact.CVRP_exact(depot, customers, demand)
    
    capacity = np.array([15])
    num_vehicles = 1
    vehicle = Exact.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    customer_order, solution, shortest_distance = cvrp.solve()
    
    print('\ncustomer visiting order:\n ', customer_order)
    print('\nsolution: ', solution)
    print('\nshortest_distance: ', shortest_distance)
    