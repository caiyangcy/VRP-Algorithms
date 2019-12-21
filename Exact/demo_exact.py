'''
Implementation of some exact algorithms.
No optimisation yet.
CVRP
'''

import numpy as np
import matplotlib.pyplot as plt
import class_info as Exact
from matplotlib.animation import FuncAnimation
from matplotlib import animation


    
def plot_solutions(depot, customers):
    plt.scatter(depot[:,0], depot[:,1], s=60, c='r', label='depot')
    plt.scatter(customers[:,0], customers[:,1], s=50, label='customers')
    
    starting_edge_x = np.concatenate((depot[:,0], np.array([customers[0, 0]])), axis=0)
    starting_edge_y = np.concatenate((depot[:,1], np.array([customers[0, 1]])), axis=0)
    plt.plot(starting_edge_x, starting_edge_y, c='#FF5733')
    
    for idx in range(1, len(customers)):
        prev_customer = customers[idx-1]
        curr_customer = customers[idx]
        
        x_coord = np.concatenate((np.array([prev_customer[0]]), np.array([curr_customer[0]])), axis=0)
        y_coord = np.concatenate((np.array([prev_customer[1]]), np.array([curr_customer[1]])), axis=0)
        
        plt.plot(x_coord, y_coord, c='#FF5733')
    
    ending_edge_x = np.concatenate((depot[:,0], np.array([customers[-1, 0]])), axis=0)
    ending_edge_y = np.concatenate((depot[:,1], np.array([customers[-1, 1]])), axis=0)
    plt.plot(ending_edge_x, ending_edge_y, c='#FF5733')
    plt.legend()
    plt.show()
    

def demo(ps=True):
    
    
    depot = np.array([[0,0]])
#    customers = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
    customers = np.array([[1,1], [1,2], [-1,2]])
    demand = np.array([1,2,3,4])
    
    cvrp = Exact.CVRP_exact(depot, customers, demand)
    
    capacity = np.array([15])
    num_vehicles = 1
    vehicle = Exact.Vehicle(capacity, num_vehicles)
    
    cvrp.fit(vehicle)
    
    customer_order, solution, shortest_distance = cvrp.solve()
    
    print('\ncustomer visiting order:\n ', customer_order)
    print('\nsolution: ', solution)
    print('\nshortest_distance: ', shortest_distance)
    
    if ps:
        plot_solutions(depot, customer_order)

if __name__ == '__main__':
    
    demo()
    