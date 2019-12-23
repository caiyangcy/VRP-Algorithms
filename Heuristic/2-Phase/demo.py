# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:51:20 2019

@author: Cai
"""
import Sweep
import numpy as np

def demo_Sweep():
    depot = np.array([[0,0]])
    customers_location = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
        
    demand = np.array([1,2,3,4])
    
    cvrp = Sweep.Sweep(depot, customers_location, demand)
    
    capacity = np.array([6])
    num_vehicles = 1
    vehicle = Sweep.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    solution = cvrp.solve()

    for idx in range(len(solution)):
        print('visiting order {}: '.format(idx), solution[idx])
        
if __name__ == "__main__":
    demo_Sweep()