import numpy as np
from threading import Thread

class Ant_Colony:
    
    class Ant(Thread):
                
        def __init__(self, pheromone_map, start_node, possible_locations, demand, 
                     capacity, distance_callback, decay=0.75, alpha=5, beta=5, gamma=5, first_pass=False):
            '''
            pheromone_map: map of pheromone from current location to the next location (pheromone of arc)
            start_node: starting location
            possible locations: array of indices showing available locations of next move
            demand: 1d array showing the demand of each customer
            capacity: represents the capacity of the vehicle
            decay: evaporation rate
            alpha: relative influence of pheromone trails
            beta: relative influence of visibility
            gamma: relative influence of capacity ratio. This parameter is problem-specific
            '''
            Thread.__init__(self)
            self.pheromone_map = pheromone_map            
            self.start_node= start_node
            self.possible_locations = possible_locations
            self.demand = demand           
            self.decay = decay
            self.alpha = alpha
            self.beta = beta   
            self.gamma = gamma 
            self.distance_travelled = 0
            self.route = []
            self.tour_complete = False
            

            self.remaining_capacity = capacity
            self.capacity = capacity
            self.distance_callback = distance_callback
            self.first_pass = first_pass
        
            self._update_route(start_node)
            self._update_possible_locations()
            
            
        def run(self):
            while self.possible_locations:
                next_location = self._pick_move()
                self._update_distance(next_location)
                self._update_route(next_location)
                self._update_possible_locations()
                
            self.tour_complete = True
            
        def _pick_move(self, Q=1):
            # Ensure visited places not not visited again      
            attractiveness = []
            total = 0
            for possbile_next_location in self.possible_locations:
                
                tau = float(self.pheromone_map[self.location][possbile_next_location])
                eta = Q/self.distance_callback(self.location, possbile_next_location)
                   
                kappa = (self.remaining_capacity + self.demand[possbile_next_location])/self.capacity 
#                kappa = 0 if kappa > 1 else kappa

                v = (tau**self.alpha)*(eta**self.beta)*(kappa**self.gamma)
                attractiveness.append(v)
                total += v
            
            if np.abs(total-0.0)<1e-7:
                choice = np.random.choice(a=np.arange(len(self.possible_locations)), size=1)[0]
            else:    
                attractiveness = np.array(attractiveness)/total
                choice = np.random.choice(a=np.arange(len(self.possible_locations)), size=1, p=attractiveness)[0]

            return self.possible_locations[choice]
               
        def get_tour(self):
            if self.tour_complete:
                return self.route
            return None
        
        def get_total_distance(self):
            if self.tour_complete:
                return self.distance_travelled
            return None
        
        def _update_route(self, new):
            self.route.append(new)         
            self.location = new
            self.remaining_capacity -= self.demand[new]
                    
        def _update_distance(self, new):
            self.distance_travelled += float(self.distance_callback(self.location, new))
            
        def _update_possible_locations(self):
            curr_capacity = self.remaining_capacity
            possible_locations = []
            for location in self.possible_locations:
                if (curr_capacity - self.demand[location] >= 0) and (location != self.location):
                    possible_locations.append(location)
            self.possible_locations = possible_locations
            
        
    def __init__(self, nodes, distance_callback, capacity, demand, start=None, elitist_num = 5, ant_count=50, alpha=5, beta=5, gamma=5, 
                 pheromone_evaporation_coefficient=.40, pheromone_constant=1, iterations=80):
        """
    		initializes an ant colony (houses a number of worker ants that will traverse a map to find an optimal route as per ACO [Ant Colony Optimization])
    		source: https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
    		
    		nodes -> is assumed to be a dict() mapping node ids to values 
    			that are understandable by distance_callback
    			
    		distance_callback -> is assumed to take a pair of coordinates and return the distance between them
    			populated into distance_matrix on each call to get_distance()
    			
    		start -> if set, then is assumed to be the node where all ants start their traversal
    			if unset, then assumed to be the first key of nodes when sorted()
    		
    		distance_matrix -> holds values of distances calculated between nodes
    			populated on demand by _get_distance()
    		
    		pheromone_map -> holds final values of pheromones
    			used by ants to determine traversals
    			pheromone dissipation happens to these values first, before adding pheromone values from the ants during their traversal
    			(in ant_updated_pheromone_map)
    			
    		ant_updated_pheromone_map -> a matrix to hold the pheromone values that the ants lay down
    			not used to dissipate, values from here are added to pheromone_map after dissipation step
    			(reset for each traversal)
    			
    		alpha -> a parameter from the ACO algorithm to control the influence of the amount of pheromone when an ant makes a choice
    		
    		beta -> a parameters from ACO that controls the influence of the distance to the next node in ant choice making
    		
    		pheromone_constant -> a parameter used in depositing pheromones on the map (Q in ACO algorithm)
    			used by _update_pheromone_map()
    			
    		pheromone_evaporation_coefficient -> a parameter used in removing pheromone values from the pheromone_map (rho in ACO algorithm)
    			used by _update_pheromone_map()
    		
    		ants -> holds worker ants
    			they traverse the map as per ACO
    			notable properties:
    				total distance traveled
    				route
    			
    		first_pass -> flags a first pass for the ants, which triggers unique behavior
    		
    		iterations -> how many iterations to let the ants traverse the map
    		
    		shortest_distance -> the shortest distance seen from an ant traversal
    		
    		shortets_path_seen -> the shortest path seen from a traversal (shortest_distance is the distance along this path)
    		"""
        #nodes
        if type(nodes) is not dict:
            raise TypeError("nodes must be dict")
            
        if len(nodes) < 1:
            raise ValueError("there must be at least one node in dict nodes")

        #create internal mapping and mapping for return to caller
        self.id_to_key, self.nodes = self._init_nodes(nodes)
        
        #create matrix to hold distance calculations between nodes
        self.distance_matrix = np.zeros((len(nodes), len(nodes)))   #self._init_matrix(len(nodes))
        
        #create matrix for master pheromone map, that records pheromone amounts along routes
        self.pheromone_map = np.zeros((len(nodes), len(nodes))) #self._init_matrix(len(nodes))
        
        #create a matrix for ants to add their pheromones to, before adding those to pheromone_map during the update_pheromone_map step
        self.ant_updated_pheromone_map = np.zeros((len(nodes), len(nodes))) #self._init_matrix(len(nodes))
		
    		#distance_callback
        if not callable(distance_callback):
            raise TypeError("distance_callback is not callable, should be method")
			
        self.distance_callback = distance_callback
    		
        # capacity
        if type(capacity) is not int:
            raise TypeError("capacity must be int")
    			
        if beta < 0:
            raise ValueError("capacity must be >= 1")
            
        self.capacity = capacity
        
        # demand
        if type(demand) is not np.ndarray:
            raise TypeError("demand must be numpy array")
            
        if demand.min() < 0:
            raise ValueError("min value of demand must be >= 0")
            
        self.deamnd = demand
        
    		#start
        if start is None:
            self.start = 0
        else:
            self.start = None
    			 #init start to internal id of node id passed
            for key, value in self.id_to_key.items():
                if value == start:
                    self.start = key
    			
    			#if we didn't find a key in the nodes passed in, then raise
            if self.start is None:
                raise KeyError("Key: " + str(start) + " not found in the nodes dict passed.")
    		
    		#ant_count
        if type(ant_count) is not int:
            raise TypeError("ant_count must be int")
    			
        if ant_count < 1:
            raise ValueError("ant_count must be >= 1")
    		
        self.ant_count = ant_count
    		
        #elitist number
        if type(elitist_num) is not int:
            raise TypeError("elitist_num must be int")
    			
        if ant_count < 0:
            raise ValueError("elitist_num must be >= 0")
    		
        if elitist_num == 0:
            elitist_num = ant_count
            
        self.elitist_num = elitist_num
        
        
    		#alpha	
        if (type(alpha) is not int) and type(alpha) is not float:
            raise TypeError("alpha must be int or float")
    		
        if alpha < 0:
            raise ValueError("alpha must be >= 0")
    		
        self.alpha = float(alpha)
    		
    		#beta
        if (type(beta) is not int) and type(beta) is not float:
            raise TypeError("beta must be int or float")
    			
        if beta < 1:
            raise ValueError("beta must be >= 1")
    			
        self.beta = float(beta)
        
        #gamma
        if (type(gamma) is not int) and type(gamma) is not float:
            raise TypeError("alpha must be int or float")
    		
        if gamma < 0:
            raise ValueError("alpha must be >= 0")
    		
        self.gamma = float(gamma)
    		
    		#pheromone_evaporation_coefficient
        if (type(pheromone_evaporation_coefficient) is not int) and type(pheromone_evaporation_coefficient) is not float:
            raise TypeError("pheromone_evaporation_coefficient must be int or float")
    		
        self.pheromone_evaporation_coefficient = float(pheromone_evaporation_coefficient)
    		
    		#pheromone_constant
        if (type(pheromone_constant) is not int) and type(pheromone_constant) is not float:
            raise TypeError("pheromone_constant must be int or float")
    		
        self.pheromone_constant = float(pheromone_constant)
    		
    		#iterations
        if (type(iterations) is not int):
            raise TypeError("iterations must be int")
    		
        if iterations < 0:
            raise ValueError("iterations must be >= 0")
    			
        self.iterations = iterations
    		
    		#other internal variable init
        self.first_pass = True
        self.ants = self._init_ants(self.start)
        self.shortest_distance = None
        self.shortest_path_seen = None
    
    def _init_nodes(self, nodes):
        id_to_key = dict()
        id_to_values = dict() # think this as a map from customer id to its demand
            
        id = 0
        for key in sorted(nodes.keys()):
            id_to_key[id] = key
            id_to_values[id] = nodes[key]
            id += 1
			
        return id_to_key, id_to_values
    
    def _init_matrix(self, size):
        return np.zeros((size, size))
        
    def _init_ants(self, start_location):
        if self.first_pass:
            return [self.Ant(self.pheromone_map, start_location, list(self.nodes.keys()), self.deamnd, 
                    self.capacity, self.distance_callback, self.pheromone_evaporation_coefficient,
                    self.alpha, self.beta, self.gamma, first_pass=True) for _ in range(self.ant_count)]
        
        else:
            for ant in self.ants:
                ant.__init__(self.pheromone_map, start_location, list(self.nodes.keys()), self.deamnd, 
                    self.capacity, self.distance_callback, self.pheromone_evaporation_coefficient,
                    self.alpha, self.beta, self.gamma)
        

    def _update_pheromone(self):
        
        shortest_length = self.shortest_distance
        shortest_route = self.shortest_path_seen
        
        for from_node in range(self.pheromone_map.shape[0]):
            for to_node in range(self.pheromone_map.shape[1]):
                self.pheromone_map[from_node, to_node] *= (1-self.pheromone_evaporation_coefficient)
                self.pheromone_map[from_node, to_node] += self.ant_updated_pheromone_map[from_node, to_node]
                
                if self.elitist_num != 0 and [from_node, to_node] in shortest_route:
                    self.pheromone_map[from_node, to_node] += self.elitist_num*(self.pheromone_constant/shortest_length)
    
    def _populate_ant_updated_pheromone_map(self, ant):
        route = ant.get_tour()
        for i in range(len(route)-1):
             curr_pher = float(self.ant_updated_pheromone_map[route[i], route[i+1]])
             new_pher = self.pheromone_constant/ant.get_total_distance()
             self.ant_updated_pheromone_map[route[i], route[i+1]] = curr_pher + new_pher
             self.ant_updated_pheromone_map[route[i+1], route[i]] = curr_pher + new_pher
            
    def solve(self):
        for i in range(self.iterations):
            for ant in self.ants:
                ant.start()
            
            for ant in self.ants:
                ant.join()
            
            for ant in self.ants:
                self._populate_ant_updated_pheromone_map(ant)
                
                if not self.shortest_distance:
                    self.shortest_distance = ant.get_total_distance()
                
                if not self.shortest_path_seen:
                    self.shortest_path_seen = ant.get_tour()
                
                if self.shortest_distance < ant.get_total_distance():
                    self.shortest_distance = ant.get_total_distance()
                    self.shortest_path_seen = ant.get_tour()
                    
            
            self._update_pheromone()
            
            if self.first_pass:
                self.first_pass = False
            
            self._init_ants(self.start)#+i%4)
            self.ant_updated_pheromone_map = np.zeros((len(self.nodes), len(self.nodes))) 
        
        result = []
        
        for id in self.shortest_path_seen:
            result.append(self.id_to_key[id])
        
        return result