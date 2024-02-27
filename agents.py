import numpy as np


class Agent:
    @staticmethod
    def is_valid_position(pos):
        return np.all(pos >= 0) and np.all(pos < 3)
    
    @staticmethod
    def get_zero_coordinate(board_state):
        return np.array(np.where(board_state==0)).reshape(2)
    
    @staticmethod
    def get_available_actions(board_state):        
        zero_pos = Agent.get_zero_coordinate(board_state)
        vertical_actions = (["down"],["up", "down"] ,["up"])
        horizontal_actions = (["right"],["left", "right"] ,["left"])
        x_coordinate = zero_pos[1]       
        y_coordinate = zero_pos[0]
        available_actions = vertical_actions[y_coordinate] + horizontal_actions[x_coordinate]
        return available_actions

    
    def __init__(self, current_state):
        self.current_state = current_state

    
    
