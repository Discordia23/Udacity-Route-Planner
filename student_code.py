import heapq
from math import sqrt

def shortest_path(M,start,goal):
    
    # heapq with (f distance, state) for each explored state - initialized with initial state (start)
    frontier = [(0, start)]
    heapq.heapify(frontier)
    
    # dict for {state: prestate} of each state - needed to retrace the shortest route
    explored = {}
    explored[start] = None # initialized with initial state (start)
    
    # dict for {state: g distance} - needed to avoid recalculation of the real distance between initial state and prestate
    g_distances = {}
    g_distances[start] = 0 # initialized with initial state (start)
    
    while frontier:
        lowest_distance, current_state = heapq.heappop(frontier) # get the route with the lowest f distance from heapq
        if current_state == goal: # loop restarts until all states in frontier have been explored
            break
        for neighbour in M.roads[current_state]:
            g = g_distances[current_state] + distance(M, current_state, neighbour) # calculation of g distance for the state 
            # if state not explored or new calculated g distance lower as already known (better route explored)
            if (neighbour not in g_distances.keys()) or (g < g_distances[neighbour]): 
                g_distances[neighbour] = g # actualize dict with g distance for this state
                f = g + distance(M, neighbour, goal) # calculate f distance for this state
                heapq.heappush(frontier, (f, neighbour)) # add (f distance, state) in heapq
                explored[neighbour] = current_state # actualize explored dict
    
    print("shortest path called")
    return result(explored, start, goal)

def result(explored, start, goal): 
    # function that takes the explored dict and retraces the shortest path backwards (from goal to start) and return the reversed route
    path_reversed = [goal]
    current = goal
    while current != start:
        path_reversed.append(explored[current])
        current = explored[current]
    path = path_reversed[::-1]
    return path


def distance(M, state1, state2):
    # function to calculate the g (real) distances or h (estimated) distances between two states
    x1, y1 = M.intersections[state1]
    x2, y2 = M.intersections[state2]
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

