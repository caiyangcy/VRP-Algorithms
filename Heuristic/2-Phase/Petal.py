import numpy as np
import time 
from scipy.optimize import linprog

class Vehicle:
    '''
    current number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity.min() > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num

class Petal:
    
    depot, customers, demand = 0, 0, 0
    split_delivery = False
    vehicle = None
    ASSIGN_MATRIX = None
    COST_MATRIX = None
    
    def __init__(self, depot, customers, demand):
        self.depot = depot
        self.customers = customers
        self.demand = demand
        
    def fit(self, v):
        self.vehicle = v
        
        if self.vehicle.capacity < self.demand.max() and not self.split_delivery:
            raise Exception("The capacity of vehicle is smaller than the maximum demand")
            self.vehicle = None
        
    def _assign_matrix(self, starting_plan):
        
        init_start = starting_plan
        curr_demand = self.demand[starting_plan]
        while curr_demand <= self.vehicle.capacity and starting_plan < self.demand.shape[0]:
            starting_plan += 1
            curr_demand += self.demand[starting_plan]
        starting_plan -= 1
        curr_demand -= self.demand[starting_plan]
        
        work_plans = np.zeros((self.customers.shape[0], starting_plan-init_start+1))
        work_plan_cost = np.zeros((starting_plan-init_start+1, ))
        
        for i in range(work_plans.shape[1]):
            work_plans[:,i][:i+1] = 1
            work_plan_cost[i] = self.demand[init_start:i+1].sum()
        
        return work_plans, work_plan_cost
    
    def _create_AM(self):
        assign_init, cost_init = self._assign_matrix(0)
        for i in range(1, self.demand.shape[0]):
            plan, cost = self._assign_matrix(i)
            assign_init = np.concatenate((assign_init, plan), axis=1)
            cost_init = np.concatenate((cost_init, cost))
        
        self.ASSIGN_MATRIX = assign_init
        self.COST_MATRIX = cost_init
        
    def _SSP_solver(self):
        '''
        This function is simply based on scipy 
        '''
        c = self.COST_MATRIX.reshape(-1, )
        A_eq = self.ASSIGN_MATRIX
        b_eq = np.ones((c.shape[0], ))
        
        bounds = (0, 1)
        
        res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
        return res
    
    def solve(self):
        
        start_time = time.time()
        
        res = self._SSP_solver()
        
        end_time = time.time()
        print('\nFinished solving, with total time %s mins \n' % ((end_time - start_time)/60))    
    
        return res.x