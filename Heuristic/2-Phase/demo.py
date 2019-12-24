# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:51:20 2019

@author: Cai
"""
import Sweep
import Petal
import numpy as np

def demo_Sweep():
    depot = np.array([[0,0]])
    customers_location = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
    customers = []
    
    label = 0
    for cl in customers_location:
        customers.append(Sweep.Customer(cl, label))
        label += 1
        
    demand = np.array([1,2,3,4])
    
    cvrp = Sweep.Sweep(depot, customers, demand)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = Sweep.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    solution, distance = cvrp.solve()

    for idx in range(len(solution)):
        print('visiting order {} : {} with distance {}'.format(idx, solution[idx], distance[idx]))
        
def demo_Petal():
    depot = np.array([[0,0]])
    customers = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
        
    demand = np.array([1,2,3,4])
    
    cvrp = Petal.Petal(depot, customers, demand)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = Petal.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    cvrp.solve()

        
if __name__ == "__main__":
#    demo_Sweep()s
    demo_Petal()