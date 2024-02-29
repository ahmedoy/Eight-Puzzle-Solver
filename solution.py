import numpy as np

class Node:
    def __init__(self, board_state, action, cost, parent=None):
        self.parent = parent
        self.board_state = board_state
        self.action = action #Action performed on the parent to reach the current state/node
        self.cost = cost
    
    def __hash__(self): #To insert the node in the dictionary for the decrease key operation
        return hash(tuple(self.board_state.flatten()))
    
    def __eq__(self, other):#To find the node in the dictionary for the decrease key operation
        return isinstance(other, Node) and tuple(self.board_state.flatten()) == tuple(other.board_state.flatten())


