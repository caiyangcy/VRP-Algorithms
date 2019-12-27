# https://github.com/pjmattingly/ant-colony-optimization

import Ant_Colony
import numpy as np


def demo_Ant():
#    customer_nodes = {0: (1, 1), 1: (1, -1), 2: (-1, 1), 3: (-1, -1)}
#    demand = np.array([1,2,3,4])
    
    customer_nodes = {0: (0, 0), 1: (1, 1), 2: (1, -1), 3: (-1, 1), 4: (-1, -1)}
    demand = np.array([0,1,2,3,4])
    
    capacity = 4
    def distance(a, b):
        if a == b:
            return np.inf
        node_a = customer_nodes[a]
        node_b = customer_nodes[b]
        return np.sqrt(np.abs(node_a[0]-node_b[0])**2 + np.abs(node_a[1]-node_b[1])**2)
    
   
    colony = Ant_Colony.Ant_Colony(nodes=customer_nodes, distance_callback=distance, capacity=capacity, demand=demand, start=0,
                                   alpha=5, beta=5, gamma=0, ant_count=10, pheromone_evaporation_coefficient=.25, iterations=10)

    result = colony.solve()+[0]
    
    print('result: \n', result)
    
    remaining_customers = {0: (0, 0)}
    new_demand = [0]
    
    for i in customer_nodes.keys():
        if i not in result:
            remaining_customers[i] = customer_nodes[i]
            new_demand.append(demand[i]) 

    new_demand = np.array(new_demand)
    
    while len(remaining_customers.keys()) != 1:
        colony = Ant_Colony.Ant_Colony(nodes=remaining_customers, distance_callback=distance, capacity=capacity, demand=new_demand, start=0,
                                   alpha=5, beta=5, gamma=0, ant_count=10, pheromone_evaporation_coefficient=.25, iterations=10)

        result = colony.solve()+[0]
    
        print('result: \n', result)
        
        remaining_customers_2 = {0: (0, 0)}
        new_demand = [0]
        
        for i in remaining_customers.keys():
            if i not in result:
                remaining_customers_2[i] = remaining_customers[i]
                new_demand.append(demand[i])
        new_demand = np.array(new_demand)        
        remaining_customers = remaining_customers_2.copy()
        
def demo_Tabu():
    '''
    This demo is ... cheating
    Assume the sum of all customers' demand is no bigger than the capacity of the vehicle
    '''
    None
    
def demo_SA():
    None

if __name__ == "__main__":
    demo_Ant()
