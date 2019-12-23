import numpy as np
import time 
import itertools
from scipy.spatial import distance_matrix

class Customer:
    coordinate = []
    angle = 0
    cluster_num = 0
    
    def _get_angle(coordinate):
        
        x = coordinate[0]
        y = coordinate[1]
        
        assert x == 0 and y == 0
        
        if x == 0:
            return 90 if y > 0 else 270
        elif y == 0:
            return 0 if x > 0 else 180
        
        angle = np.degrees(np.arctan(np.abs(y/x)))
        
        if x > 0 and y > 0:
            return angle
        elif x < 0 and y < 0:
            return angle + np.pi
        elif x < 0 and y > 0:
            return angle + np.pi/2
        
        return angle + np.pi*3/2
        
        
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self._get_angle(coordinate)

class Vehicle:
    '''
    current number of vehicles is limited to 1
    '''
    capacity, num = 0, 0
    
    def __init__(self, capacity, num=1):
        assert capacity.min() > 0 and num > 0 and num%1 == 0, "invalid vehicle info"
        self.capacity = capacity
        self.num = num

class Sweep:
    
    depot, customers, demand, customers_location = 0, 0, 0, 0
    split_delivery = False
    vehicle = None
    
    def __init__(self, depot, customers, demand):
        self.depot = depot
        self.customers = customers
        self.demand = demand
        
        self.customers_location = np.array([c.coordinate for c in customers])
    
    def _sort_by_angle(self):
        angles = np.array([c.angle for c in self.customers])
        angles_arg = angles.argsort()
        return angles_arg
    
    def cluster(self):
        angles_arg = self._sort_by_angle()
        sorted_customers = self.customers[angles_arg]
        demand = self.demand[angles_arg]
        cluster_num, curr_demand, i = 0, 0, 0
        
        

        while i < sorted_customers.shape[0] or curr_demand <= self.vehicle.capacity:
            if curr_demand + demand[i] > self.vehicle.capacity:
                cluster_num += 1
                curr_demand = 0
                
            curr_demand += demand[i]
            sorted_customers[i].cluster_num = cluster_num
            i += 1
         
        clusters = np.zeros((cluster_num+1, 1))    
        for c in self.customers:
            clusters[c.cluster_num] = np.append(clusters[c.cluster_num], np.array([c.coordinate]))
         
        return clusters
    
    def _TSP_Exact(self, cluster):
        data = np.concatenate((self.depot, cluster), axis=0)
        cluster_dm = distance_matrix(data, data)
        solution = []
        best_distance = np.inf
        
        choices = list(itertools.permutations(np.arange(1, cluster.shape[0]+1, 1)))
        choices = choices[:len(choices)//2]
        for choice in choices:
  
            total_distance = cluster_dm[0, choice[0]] # from depot to first customer

            for idx in range(1, len(choice)):
                total_distance += cluster_dm[choice[idx-1], choice[idx]]
            total_distance += cluster_dm[choice[-1], 0] # from last customer to depot
            if total_distance < best_distance:
                best_distance = total_distance
                solution = choice
                    
        return solution, best_distance # solution is based on index of each customer in cluster
        
    def solve(self):
        start_time = time.time()
        clusters = self.cluster()
        solutions = []
        distances = []
        
        for cls in clusters:
            tsp_solution, best_distance = self._TSP_Exact(cls)
            solutions.append(tsp_solution)
            distances.append(best_distance)
            
        end_time = time.time()
        print('\nFinished solving, with total time %s mins \n' % ((end_time - start_time)/60))    
    
        return solutions