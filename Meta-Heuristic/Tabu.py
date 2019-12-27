import numpy as np
import time
import random

class Tabu:
    def __init__(self, customer, demand, tabu_tenure, tabu_size):
        '''
        customer is a dictionary
        '''
        self.customer = customer
        self.demand = demand
        self.TABU_TENURE = tabu_tenure
        self.TABU_SIZE = tabu_szie
        self.s0 = self._generate_init_solution()
        
    def _euclidean_dist(self, a, b):
        if a == b:
            return np.inf
        node_a = self.customer[a]
        node_b = self.customer[b]
        return np.sqrt(np.abs(node_a[0]-node_b[0])**2 + np.abs(node_a[1]-node_b[1])**2)
    
    def _generate_init_solution(self):
        '''
        Generating the initial solution randomly
        '''
        customers = self.customer.keys()
        init_solution = random.shuffle(customers)
        if init_solution[0] != 0:
            for i in range(len(init_solution)):
                if init_solution[i] == 0:
                    init_solution[i] = init_solution[0]
        init_solution[0] = 0
        init_solution += [0]
        
        return init_solution
    
    def _two_opt_swap(self, candidate_solution, i, k):

        before = candidate_solution[:i]
        after = candidate_solution[k+1:]
        new_solution = before + candidate_solution[k:i-1:-1] + after
        
        return new_solution
    
    def two_opt(self, curr_solution):
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
        
    def _evaluate(self, solution):
        sum_distance = 0
        for idx in range(1, len(solution)):
            sum_distance += self._euclidean_dist(solution[idx], solution[idx-1])
        return sum_distance
    
    def tabu_search(self):
        stop = False
        best_solution_kept = 0
        best_solution = self.s0
        best_candidate = self.s0
        tabu_list = []
        while not stop:
            candidate_solution, candidate_distance = self.two_opt(best_candidate)
            
            if candidate_distance < self._evaluate(best_candidate) and candidate_solution not in tabu_list:
                best_candidate = candidate_solution
            
            if candidate_distance < self._evaluate(best_solution):
                best_solution = candidate_solution
                best_solution_kept = 0
                
            best_solution_kept += 1
                
            tabu_list.append(candidate_solution)
            
            if len(tabu_list) > self.TABU_SIZE:
                tabu_list.pop(0)
                
            if best_solution_kept == self.TABU_TENURE:
                stop = True
                
        return best_solution