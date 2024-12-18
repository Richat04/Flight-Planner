from flight import Flight

from heap import Heap , comp1, comp2

class Planner:
    def __init__(self, flights):
        """The Planner
        
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """

        n = 0
        for i in flights:
            if i.end_city > n:
                n = i.end_city
        self.adjacency_list = [[] for i in range(n+1)]
        for i in flights:
            
            self.adjacency_list[i.start_city].append(i)  #city meri vertex aur flight meri edge
        
        self.num_of_city = n+1
        self.num_flight = len(flights)
        
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city:
            return []
        if t1 == t2:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        positive_list = []  #actual list      #0 ki jagah t1 because my time starts from t1
        negative_list = []      # list made only for pop to run in O(1)

        visited = [False]*self.num_flight
        best_case = [float('inf'), float('inf'), None]
        path = [None]*self.num_flight
        # q= []
        for i in self.adjacency_list[start_city]:
            if i.departure_time >= t1 and i.arrival_time <=t2:
                positive_list.append([0, i.arrival_time, i.end_city, i])
                visited[i.flight_no] = True
        

        while len(positive_list) != 0 or len(negative_list) != 0:
            if len(negative_list) == 0:
                while len(positive_list) != 0:
                    negative_list.append(positive_list.pop())

            num_o_flights , arrival_time, city, aero = negative_list.pop()
            if city == end_city:
                if (num_o_flights< best_case[0]) or (num_o_flights == best_case[0] and arrival_time < best_case[1]):
                    best_case = [num_o_flights , arrival_time , aero]   

            else:
                if self.adjacency_list[city] == None:
                    break
                else:

                    for i in self.adjacency_list[city]:
                        if visited[i.flight_no] != True and (i.departure_time >= arrival_time +20) and (i.arrival_time <= t2):
                            positive_list.append([num_o_flights+1, i.arrival_time, i.end_city, i])
                            path[i.flight_no] = aero
                            visited[i.flight_no] = True

        # print(best_case[-1])
        if best_case[-1] == None:
            return []
        else:
            optimal = [best_case[-1]]
            i = best_case[-1].flight_no
            while True:
                if path[i] == None:
                    l=[]
                    for i in range(len(optimal)-1,-1,-1):
                        l.append(optimal[i])
                    # print(optimal[::-1])
                    return l
                else:
                    optimal.append(path[i])
                    i = path[i].flight_no
        # return self.path_tracker(best_case, path)  


     

        
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city:
            return []
        if t1 == t2:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        visited = [False]*self.num_flight
        best_case = [float('inf'), None]
        flight_path = [None]*self.num_flight
        myheap = Heap(comparison_function=comp1 , init_array=[])
        
        
        for i in self.adjacency_list[start_city]:
            if i.departure_time >= t1 and i.arrival_time <=t2:
                myheap.insert([i.fare, i.end_city, i])
                visited[i.flight_no] = True
        
                
        # visited = [None]*self.num_of_city
        
        
        while myheap.length() != 0:
            fare, city, aero = myheap.extract()
            # print(arrival_time)

            if city == end_city:
                if fare < best_case[0]:
                    best_case = [fare, aero]
                
            else:
                if self.adjacency_list[city] == None:
                    break
                else:

                    for i in self.adjacency_list[city]:
                        if visited[i.flight_no] != True and (i.departure_time >= aero.arrival_time + 20) and (i.arrival_time <= t2):
                            myheap.insert([fare + i.fare, i.end_city, i])
                            flight_path[i.flight_no] = aero
                            visited[i.flight_no] = True

        if best_case[-1] == None:
            return []
        else:
            optimal = [best_case[-1]]
            i = best_case[-1].flight_no
            while True:
                if flight_path[i] == None:
                    l=[]
                    for i in range(len(optimal)-1,-1,-1):
                        l.append(optimal[i])
                    # print(optimal[::-1])
                    return l
                else:
                    optimal.append(flight_path[i])
                    i = flight_path[i].flight_no

                
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city:
            return []
        if t1 == t2:
            return []
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        flight_path = [None]*self.num_flight
        heap = Heap(comparison_function=comp2, init_array= [])
        best_case = [float('inf'), float('inf'), None]
        # heap.print_heap()
        visited = [False]*self.num_flight

        for i in self.adjacency_list[start_city]:
            if i.departure_time >= t1 and i.arrival_time <=t2:
                heap.insert([0,i.fare, i.end_city, i])
                visited[i.flight_no] = True



        while heap.length() != 0:

            flight_count , fare , city , aero = heap.extract()

            if city == end_city:
                if flight_count < best_case[0] or (flight_count == best_case[0] and fare < best_case[1]):
                    best_case = [flight_count, fare, aero]

            else:
                if self.adjacency_list[city] == None:
                    break
                else:

                    for i in self.adjacency_list[city]:
                        if visited[i.flight_no] != True and (i.departure_time >= aero.arrival_time + 20) and (i.arrival_time <= t2):
                            heap.insert([flight_count + 1, fare + i.fare, i.end_city, i])
                            flight_path[i.flight_no] = aero
                            visited[i.flight_no] = True

        if best_case[-1] == None:
            return []
        else:
            optimal = [best_case[-1]]
            i = best_case[-1].flight_no
            while True:
                if flight_path[i] == None:
                    l=[]
                    for i in range(len(optimal)-1,-1,-1):
                        l.append(optimal[i])
                    # print(optimal[::-1])
                    return l
                else:
                    optimal.append(flight_path[i])
                    i = flight_path[i].flight_no
            