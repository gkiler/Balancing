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

    def find_weights(self):
        # get width
        ship_width = ...
        l_start = 0
        r_start = ship_width / 2 + 1
        left_weight = 0
        right_weight = 0
        # for container in left half of ship:
            # left_weight += weight
        # for container in right half of ship:
            # right_weight += weight 
        if left_weight > right_weight:
            is_left = True
        else:
            is_left = False
        return left_weight, right_weight, is_left

    def expand(self,seen_set):
        # expand the set by finding all of the spaces surface
        # containers can be moved to
        width = ...
        _,_,is_left = self.find_weights()
        # use same function as used in is_goal()
        # which side is the heavier half?
        if is_left:
            l_start = 0
            r_start = width / 2 + 1
        else:
            l_start = width / 2 + 1
            r_start = width
        # for l_start -> r_start:
            # for top to bottom:
                # if self.state[x,y] not empty:
                    # to_test_set.append(state[x,y])
        # nearest_space = find_nearest_space(self.state, edge of half position) 
        # for container in expand_set:
            # new_state = copy.copy(self.state)
            # new_state.swap(nearest_space, container.position)
            # if new_state.tobytes() not in seen_set:
                # expand_set.append((new_state,container.position,nearest_space)) # to store to/from pos
        # return expand_set        

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



 