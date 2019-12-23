import numpy as np
import time
from scipy.spatial import distance_matrix

class Customer:
    coordinate = []
    belong_to_route = False
    is_endpoint = True
    
    def __init__(self, coordinate):
        self.coordinate = coordinate

class Vehicle:
    '''
    current number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity.min() > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num
        
class Clark_Wright_Parallel:
    # depot and customers should be a 2d array
    depot, customers, demand, customer_location = 0, 0, 0, 0
    split_delivery = False
    vehicle = None
    CWSM = None # This is a lower left triangular
    DM = None # distance matrix
    
    def __init__(self, depot, customers, demand, customer_location):
        self.depot = depot
        self.customers = customers
        self.demand = demand
        self.customer_location = customer_location
        
    def fit(self, v):
        self.vehicle = v
        
        if self.vehicle.capacity < self.demand.max() and not self.split_delivery:
            raise Exception("The capacity of vehicle is smaller than the maximum demand")
            self.vehicle = None
                      
    def _init_saving_matrix(self):
        # The first row is depot
        mat_size = self.customer_location.shape[0] #+self.depot.shape[0]
        CWSM = np.zeros((mat_size, mat_size))
        DM = self.DM
        from_node_idx = 0
        while from_node_idx != mat_size:
            for i in range(from_node_idx+1, mat_size):
                CWSM[i,from_node_idx] = DM[0, from_node_idx+1] + DM[i+1, 0] - DM[i+1, from_node_idx+1]
            from_node_idx += 1

        self.CWSM = CWSM
        
    def _parallel_solve(self):
        
        SM = self.CWSM.copy()
        customers_info = self.customers.copy()
        
        solution_set = [[]]*self.customer_location.shape[0]
        for i in range(len(solution_set)):
            solution_set[i] = [i]
            
        routes_capacity = self.demand.copy()
        
        while np.amax(SM) > 0:
            
            print('\nBefore: ', solution_set)
            
            max_savings = np.where(SM == np.amax(SM))
            max_savings_idx = list(zip(max_savings[0], max_savings[1]))[0] # Pick up the first index
            print('max_savings_idx: ', max_savings_idx)
            is_endpoint = customers_info[max_savings_idx[0]].is_endpoint and customers_info[max_savings_idx[1]].is_endpoint

            max_savings_idx = list(max_savings_idx)
            max_savings_idx.sort()
            
            if (sum(routes_capacity[max_savings_idx]) <= self.vehicle.capacity) and is_endpoint:
                
                smaller = max_savings_idx[0]
                larger = max_savings_idx[1]
                
                routes_capacity[smaller] += routes_capacity[larger]
#                routes_capacity.remove(routes_capacity[larger])
                
                solution_set[smaller] += solution_set[larger]
                
                for i in range(1, len(solution_set[smaller])-1):
                    customers_info[solution_set[smaller][i]].is_endpoint = False
                    
                solution_set.remove(solution_set[larger])
                
            for idx in range(1, len(max_savings_idx)):
                SM[max_savings_idx[idx], max_savings_idx[idx-1]] = -np.inf
                       
            if len(solution_set[smaller]) > 2:
#                print('if clause: ', curr_solution)
#                print('middle point: ', curr_solution[1:curr_solution.size-1])
                middle_points = [int(i) for i in solution_set[smaller][1:len(solution_set[smaller])-1]]
                
                SM[:, middle_points] = -np.inf     
                
            print('After: ', solution_set)
            
        self.customer = customers_info
        
        return solution_set
    
    def solve(self):
        '''
        solver: parallel or sequential
        '''
        
        start_time = time.time()
        
        depot, customers = self.depot, self.customer_location
        
        data = np.concatenate((depot, customers), axis=0)
        self.DM = distance_matrix(data, data)
        print('Distance Matrix: \n', self.DM)
        self._init_saving_matrix()
        print('\nInitial Savings Matrix: \n', self.CWSM)
        
        solutions = self._parallel_solve()
        
        end_time = time.time()
        print('\nFinished solving, with total time %s mins \n' % ((end_time - start_time)/60))
        
        return solutions
        
        