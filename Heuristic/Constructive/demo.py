'''
Implementation of Clarke Wright Savings Algorithm.
No optimisation yet.
CVRP
'''

import numpy as np
import matplotlib.pyplot as plt
import Clarke_Wright as CW
from matplotlib.animation import FuncAnimation
from matplotlib import animation

    

def demo(ps=True, solver='sequential'):
    depot = np.array([[0,0]])
    customers = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
#    customers = np.array([[1,1], [1,2], [-1,2]])
    demand = np.array([1,2,3,4])
    
    cvrp = CW.Clark_Wright(depot, customers, demand)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = CW.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    solution = cvrp.solve()
    
#    print('\ncustomer visiting order:\n ', customer_order)
    print('\nsolution: ', solution)
#    print('\nshortest_distance: ', shortest_distance)
    

if __name__ == '__main__':
    
    demo()
    