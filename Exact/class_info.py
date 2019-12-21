# Class info

'''
Implementation of some exact algorithms.
No optimisation yet.
CVRP
'''
import time
from scipy.spatial import distance_matrix
import itertools
import numpy as np

class CVRP_exact:
    # depot and customers should be a 2d array
    depot, customers, demand = 0, 0, 0
    split_delivery = False
    vehicle = None
    
    def __init__(self, depot, customers, demand):
        self.depot = depot
        self.customers = customers
        self.demand = demand
#        self.split_delivery = split
        
    def fit(self, v):
        '''
        v: The vehicle used to solve the current delivery. It contains info on numbers and capacities.
        '''
        self.vehicle = v
        
        if self.vehicle.capacity < self.demand.max() and not self.split_delivery:
            raise Exception("The capacity of vehicle is smaller than the maximum demand")
            self.vehicle = None
            
        
        
    def solve(self):
        '''
        solver = branch and bound(bnb) or branch and cut(bnc)
        '''
        if self.vehicle == None:
            raise Exception("No vehicle info found")
        
        print('Start solving')
        
        start_time = time.time()
        
        depot, customers = self.depot, self.customers
        
        data = np.concatenate((depot, customers), axis=0)
        dm = distance_matrix(data, data)
        solution = []
        best_distance = np.inf
        
        choices = list(itertools.permutations(np.arange(1, customers.shape[0]+1, 1)))
        choices = choices[:len(choices)//2]
        for choice in choices:
  
            total_distance = dm[0, choice[0]] # from depot to first customer

            for idx in range(1, len(choice)):
                total_distance += dm[choice[idx-1], choice[idx]]
            total_distance += dm[choice[-1], 0] # from last customer to depot
            if total_distance < best_distance:
                best_distance = total_distance
                solution = choice
            
        end_time = time.time()
        print('\nFinished solving, with total time %s mins ' % ((end_time - start_time)/60))
        
        solution = np.array(solution)
        print('solution: ', solution)
        return customers[solution-1], solution, best_distance
        
class Vehicle:
    '''
    current;y, number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity.min() > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num
        