# Class info

'''
Implementation of some exact algorithms.
No optimisation yet.
CVRP
'''
import time
from scipy.spatial import distance_matrix
import itertools

class CVRP_exact:
    
    depot, customers, demand = 0, 0
    split_delivery = False
    vehicle = None
    
    def __init__(self, depot, customers, demand, split):
        self.depot = depot
        self.customers = customers
        self.demand = demand
        self.split_delivery = split
        
    def fit(v):
        '''
        v: The vehicle used to solve the current delivery. It contains info on numbers and capacities.
        '''
        if vehicle.capacity < demand.sum() and not split_delivery:
            raise Exception("The capacity of vehicle is smaller than the maximum demand")
            
        else:
            vehicle = v
       
        
    def solve():
        '''
        solver = branch and bound(bnb) or branch and cut(bnc)
        '''
        if vehicle == None:
            raise Exception("No vehicle info found")
        
        print('Start solving')
        
        start_time = time.time()
        
        data = np.concatenate((depot, customers), axis=0)
        dm = distance_matrix(data, data)
        
        solution = []
        best_distance = np.sum(dm[0])
        
        choices = list(itertools.permutations(np.arange(1, customers.shape[0]+1, 1)))
        
        for choice in choices:
            total_distance = 0
            
            total_distance += dm[0, choice[0]-1] # distance between depot and the first customer
            for idx in range(len(choice)-1):
                total_distance += dm[idx-1, idx]
            total_distance += dm[choice[-1]-1, 0]
            
            if total_distance > best_distance:
                best_distance = total_distance
                solution = choice
            
        end_time = time.time()
        print('Finished solving, with total time %s mins ' % ((end_time - start_time)/60))
        
        return solution
        
        
class vehicle:
    '''
    current;y, number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num
        