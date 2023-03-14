import numpy as np
from queue import PriorityQueue

#problem state
class Ship():
    def __init__(self, containers):
        self.containers = containers

class Problem:
    def __init__(self, problem_state):
        self.seen_set = set()
        self.init = ...
        self.solution = [] #list of string instructinos
        self.queue = PriorityQueue()

    #functions inspired by my previous work in cs170 with A* Search
    def add_action(self,action):
        self.solution.append(action)
        return
    
    def push(self,node):
        self.queue.put((node.cost,node))
        return

    def pop(self):
        return self.queue.get()
        
    def is_goal(left,right):
        # expand on this...
        balance = abs(1.0*(left - right)) # define left - right weight sums
        return (balance == .1*left and balance == .1*right)
    
class Node():
    def __init__(self, parent, action, state, cost):
        self.action = action # what action was just taken, in text form i.e. "walmart 1,2 to 2,3"
        self.parent = parent # reference to parent node
        self.state = state # current state
        self.cost = parent.cost + cost
        self.depth = parent.depth + 1
    
    def __lt__(self,node):
        return self.cost < node.cost

    def expand(self,seen_set):
        return ... # todo

    # cost function (manhattan distance)
    def find_cost(pos1,pos2):
        return (abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])) # x and y
    
# pass ship state and container starting position to retrieve where to move it
def find_nearest_space(ship_state, start_pos):
    # a qualifying space must minimize distance moved to the other side
    # and not be floating

    # algorithm:
    # get ship width
    # is start_pos on left or right? (x coord is < or >= to width/2 + 1)
        # iterate over the ship spaces from 
        # bottom up left to right 
        # or right to left respectively
        # is this space empty? its not floating implicitly so we dont need to check
            # if yes, return that position
    # figure out what to do if this all messes up and there's no free space
    return ...

#start state

#goal state

#heuristic 



 