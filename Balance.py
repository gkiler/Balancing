import numpy as np


#problem state
class Ship():
    def __init__(self, containers):
        self.containers = containers

class Problem:
    def __init__(self, problem_state):
        self.seen_set = set()
        self.init = ...
        
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
        

    #cost function (manhattan distance)
    def find_cost(pos1,pos2):
        return (abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])) #x and y

#start state

#goal state

#heuristic 



 