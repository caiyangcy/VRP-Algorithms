import numpy as np
import time
from scipy.spatial import distance_matrix


class Vehicle:
    '''
    current;y, number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity.min() > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num
        
class Clark_Wright_Sequential:
    # depot and customers should be a 2d array
    depot, customers, demand = 0, 0, 0
    split_delivery = False
    vehicle = None
    CWSM = None # This is a lower left triangular
    DM = None # distance matrix
    
    def __init__(self, depot, customers, demand):
        self.depot = depot
        self.customers = customers
        self.demand = demand
        
    def fit(self, v):
        self.vehicle = v
        
        if self.vehicle.capacity < self.demand.max() and not self.split_delivery:
            raise Exception("The capacity of vehicle is smaller than the maximum demand")
            self.vehicle = None
            
            
    def _init_saving_matrix(self):
        # The first row is depot
        mat_size = self.customers.shape[0] #+self.depot.shape[0]
        CWSM = np.zeros((mat_size, mat_size))
        DM = self.DM
        from_node_idx = 0
        while from_node_idx != mat_size:
            for i in range(from_node_idx+1, mat_size):
                CWSM[i,from_node_idx] = DM[0, from_node_idx+1] + DM[i+1, 0] - DM[i+1, from_node_idx+1]
            from_node_idx += 1

        self.CWSM = CWSM
        
    def _sequential_solve(self):
        SM = self.CWSM.copy()
        curr_demand = 0
        solution_set = []
        curr_solution = np.array([])
        while np.amax(SM) > 0:
            
            overcapacity = False
            
            if curr_solution.size > 0: # There are endpoints in the array
                sub_SM = SM[:,[int(curr_solution[0]), int(curr_solution[-1])]]
                max_savings = np.amax(sub_SM)     
                _temp_is_holder = np.where(sub_SM == np.amax(sub_SM))
                savings_idx = (np.array([_temp_is_holder[0][0]]), np.array([_temp_is_holder[1][0]]))
                
            else:
                max_savings = np.amax(SM)            
                _temp_is_holder = np.where(SM == np.amax(SM))
                savings_idx = (np.array([_temp_is_holder[0][0]]), np.array([_temp_is_holder[1][0]]))
                
            # max_savings_idx is a tuple
            max_savings_idx = list(zip(savings_idx[0], savings_idx[1]))[0] # Pick up the first index
            
            new_demand = 0
            for idx in max_savings_idx:
                if idx not in curr_solution:
                    new_demand += self.demand[idx] 
                    
#            print('current demand: ', curr_demand)        
#            print('new demand: ', new_demand)
#            print('max_saving_idx: ', max_savings_idx)
            
            max_savings_idx = list(max_savings_idx)
            max_savings_idx.sort()
                
            if (curr_demand + new_demand <= self.vehicle.capacity) and (max_savings > 0):
                curr_demand += new_demand 
               
                curr_solution = np.unique(np.append(curr_solution, np.array(max_savings_idx)))
                
            else:
                overcapacity = True
                if curr_solution.size > 0:
                    solution_set.append(curr_solution)
                curr_solution = np.array([])
                curr_demand = 0

            for idx in range(1, len(max_savings_idx)):
                SM[max_savings_idx[idx], max_savings_idx[idx-1]] = -np.inf
                
            if curr_solution.size > 2:
#                print('if clause: ', curr_solution)
#                print('middle point: ', curr_solution[1:curr_solution.size-1])
                SM[:, [curr_solution[1:curr_solution.size-1].astype(int)]] = -np.inf     
        
        if not overcapacity:
            solution_set.append(curr_solution)
            
        for c in range(len(self.customers)):
            is_in = False
            for s in solution_set:
                if c in s:
                    is_in = True
                    break
            if not is_in:
                solution_set.append(np.array([int(c)]))
                
        solution_set = [i.astype(int) for i in solution_set]
        return np.array(solution_set)
    
            
    def solve(self):
        '''
        solver: parallel or sequential
        '''
        
        start_time = time.time()
        
        depot, customers = self.depot, self.customers
        
        data = np.concatenate((depot, customers), axis=0)
        self.DM = distance_matrix(data, data)
        print('Distance Matrix: \n', self.DM)
        self._init_saving_matrix()
        print('\nInitial Savings Matrix: \n', self.CWSM)
        
        solutions = self._sequential_solve()
        
        end_time = time.time()
        print('\nFinished solving, with total time %s mins \n' % ((end_time - start_time)/60))
        
        return solutions
        
        