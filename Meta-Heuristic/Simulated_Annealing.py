import numpy as np
import time
import random

class SA:
    
    def __init__(self, customer, demand, init_temperature=5000, reduction_multiplier=0.99, iteration_multiplier=1.05, update_gap=5, max_time):
        self.CUSTOMER = customer
        self.DEMAND = demand
        self.T = init_temperature
        self.alpha = reduction_multiplier
        self.beta = iteration_multiplier
        self.M0 = update_gap
        self.S0 = self._generate_init_solution()
        self.MAX_TIME = max_time
        
    def _generate_init_solution(self):
        '''
        Generating the initial solution randomly
        '''
        customers = self.CUSTOMER.keys()
        init_solution = random.shuffle(customers)
        if init_solution[0] != 0:
            for i in range(len(init_solution)):
                if init_solution[i] == 0:
                    init_solution[i] = init_solution[0]
        init_solution[0] = 0
        init_solution += [0]
        
        return init_solution
    
    def _euclidean_dist(self, a, b):
        if a == b:
            return np.inf
        node_a = self.customer[a]
        node_b = self.customer[b]
        return np.sqrt(np.abs(node_a[0]-node_b[0])**2 + np.abs(node_a[1]-node_b[1])**2)
    
    def _evaluate(self, solution):
        sum_distance = 0
        for idx in range(1, len(solution)):
            sum_distance += self._euclidean_dist(solution[idx], solution[idx-1])
        return sum_distance
    
    def _two_opt_swap(self, candidate_solution, i, k):

        before = candidate_solution[:i]
        after = candidate_solution[k+1:]
        new_solution = before + candidate_solution[k:i-1:-1] + after
        
        return new_solution
    
    def _two_opt(self, curr_solution):
        '''
        Here the current solution is fixed and used to find a good solution
        There might be implementation like change the current one to the best one found 
        and use the best one to continue the search
        '''
        best_solution = curr_solution
        best_distance = self._evaluate(curr_solution)
        eligible_nodes_num = len(curr_solution)
        for i in range(1, eligible_nodes_num-1):
            for k in  range(i+2, eligible_nodes_num):
                swapped_solution = self._two_opt_swap(curr_solution, i, k)
                swapped_distance = self._evaluate(swapped_solution)
                if swapped_distance < best_distance:
                    best_distance = swapped_distance
                    best_solution = swapped_solution
        return best_solution, best_distance
    
    def SA(self):
        alpha = self.alpha
        beta = self.beta
        M0 = self.M0
        T = self.T
        current_solution = self.S0
        current_cost = self._evaluate(current_solution)
        best_solution = self.S0
        best_cost = current_cost
        time = 0
        max_time = self.MAX_TIME # Haven't figured out what this variable is
        
        while time > max_time and T > 0.001:
            M = M0
            while M >= 0:
                new_solution = self._two_opt(current_solution)
                new_cost = self._evaluate(new_solution)
                delta_cost = new_cost - current_cost
                if delta_cost < 0:
                    current_solution = new_solution
                    current_cost = new_cost
                    if new_cost < best_cost:
                        best_solution = current_solution
                        best_cost = current_cost
                else:
                    random = np.random.random_sample() # Boltzmann
                    if random < (np.e)**(-delta_cost/T):
                        current_solution = new_solution
                        current_cost = new_cost
                M -= 1
            
            time += M0
            T *= alpha
            M0 *= beta
        
        return best_solution
        