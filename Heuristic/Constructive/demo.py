'''
Implementation of Clarke Wright Savings Algorithm.
No optimisation yet.
CVRP
'''

import numpy as np
import matplotlib.pyplot as plt
import CW_sequential as CWS
import CW_parallel as CWP
from matplotlib.animation import FuncAnimation
from matplotlib import animation

    
def demo_S():
    depot = np.array([[0,0]])
    customers = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
#    customers = np.array([[1,1], [1,2], [-1,2]])

    demand = np.array([1,2,3,4])
    
    cvrp = CWS.Clark_Wright_Sequential(depot, customers, demand)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = CWS.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    solution = cvrp.solve()

    for idx in range(len(solution)):
        print('visiting order {}: '.format(idx), solution[idx])
   
def demo_P():
    depot = np.array([[0,0]])
    customers_location = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
    customers = []
    
    for cl in customers_location:
        customers.append(CWP.Customer(cl))
        
    demand = np.array([1,2,3,4])
    
    cvrp = CWP.Clark_Wright_Parallel(depot, customers, demand, customers_location)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = CWP.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    solution = cvrp.solve()

    for idx in range(len(solution)):
        print('visiting order {}: '.format(idx), solution[idx])
    
if __name__ == '__main__':
    
#    demo_S()
    demo_P()
    