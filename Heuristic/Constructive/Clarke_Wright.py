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
        
        
        
class Clark_Wright:
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
        mat_size = self.customers.shape[0]+self.depot.shape[0]
        CWSM = np.zeros((mat_size, mat_size))
        DM = self.DM
        from_node_idx = 0
        while from_node_idx != mat_size:
            for i in range(from_node_idx+1, mat_size):
                CWSM[i,from_node_idx] = DM[0, from_node_idx] + DM[i, 0] - DM[i, from_node_idx]
            from_node_idx += 1

        self.CWSM = CWSM
    
    def _recal_SM(self):
        None
        
    def _parallel_solve(self):
        SM = self.CWSM.copy()

        solution_set = [[]]*self.customers.shape[0]
        endpoint_check = np.ones((self.customers.shape[0], ))
        routes_capacity = self.demand.copy()
        
        while np.amax(SM) > 0:
            max_savings = np.where(SM == np.amax(SM))
            max_savings_idx = list(zip(max_savings[0], max_savings[1]))[0] # Pick up the first index
            
            is_endpoint = endpoint_check[max_savings_idx[0]] and endpoint_check[max_savings_idx[1]]
            
            if (sum(routes_capacity[max_savings_idx]) < self.vehicle.capacity) and is_endpoint:
                smaller = min(max_savings_idx)
                larger = max(max_savings_idx)
                
                routes_capacity[smaller] += routes_capacity[larger]
                routes_capacity.remove(routes_capacity[larger])
                
                endpoint_check[solution_set[smaller][1:]] = 0
                endpoint_check[solution_set[larger][:-1]] = 0
                
                solution_set[smaller] += solution_set[larger]
                solution_set.remove(solution_set[larger])
            
            SM[:, max_savings_idx] = -np.inf 
        
        return solution_set
        
    def _sequential_solve(self):
        SM = self.CWSM.copy()
        curr_demand = 0
        solution_set = []
        curr_solution = np.array([])
        while np.amax(SM) > 0:
            
            if curr_solution.size > 0: # There are endpoints in the array
#                print(curr_solution[0])
#                print(curr_solution[1])
                sub_SM = SM[[int(curr_solution[0]), int(curr_solution[-1])],:]
                max_savings = np.amax(sub_SM)     
                _temp_is_holder = np.where(sub_SM == np.amax(sub_SM))
                savings_idx = (np.array([_temp_is_holder[0][0]]), np.array([_temp_is_holder[1][0]]))
                
            else:
                max_savings = np.amax(SM)            
                _temp_is_holder = np.where(SM == np.amax(SM))
                savings_idx = (np.array([_temp_is_holder[0][0]]), np.array([_temp_is_holder[1][0]]))
                
            # max_savings_idx is a tuple
            max_savings_idx = list(zip(savings_idx[0], savings_idx[1]))[0] # Pick up the first index
            d1, d2 = self.demand[max_savings_idx[0]-1], self.demand[max_savings_idx[1]-1]
            
            if (curr_demand + d1 + d2 < self.vehicle.capacity) and (max_savings > 0):
                curr_demand += d1+d2 
                # If two customers are already part of a route, 
                # then any other routes should never include them
                # -inf is used to prevent that
                
                curr_solution = np.append(curr_solution, np.array(max_savings_idx))
            else:
                solution_set.append(curr_solution)
                curr_solution = np.array([])
                curr_demand = 0
                
            SM[:, max_savings_idx] = -np.inf     
            
        solution_set = [i.astype(int) for i in solution_set]
        return np.array(solution_set)
                
    def solve(self, solver='sequential'):
        '''
        solver: parallel or sequential
        '''
        
        start_time = time.time()
        
        depot, customers = self.depot, self.customers
        
        data = np.concatenate((depot, customers), axis=0)
        self.DM = distance_matrix(data, data)
        
        self._init_saving_matrix()
        print('Savings Matrix: \n', self.CWSM)
        
        solutions = []
        if solver == 'parallel':
            print('Parallel solver set')
            solutions = self._parallel_solve()
        elif solver == 'sequential':
            print('Sequential solver set')
            solutions = self._sequential_solve()
        else:
            raise Exception("No solver found")
            
        
        end_time = time.time()
        print('\nFinished solving, with total time %s mins ' % ((end_time - start_time)/60))
        
        
        return solutions
        
        