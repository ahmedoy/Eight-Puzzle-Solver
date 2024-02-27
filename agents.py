import numpy as np

#Base Class for Agents to inherit from
class Agent:
    action_dict = {'up':np.array([-1,0]), 'down':np.array([1,0]), 'right':np.array([0,1]), 'left':np.array([0,-1]) }
    target_state = np.arange(9).reshape(3,3)    
    @staticmethod
    def is_valid_position(pos):
        return np.all(pos >= 0) and np.all(pos < 3)
    
    @staticmethod
    def get_zero_coordinate(board_state):
        return np.array(np.where(board_state==0)).reshape(2)

    @staticmethod
    def execute_action(board_state, action):
        coordinate_change = Agent.action_dict[action]
        zero_coordinate =   Agent.get_zero_coordinate(board_state) 
        new_position = coordinate_change + zero_coordinate
        zero_coordinate = tuple(zero_coordinate)
        new_position = tuple(new_position)
        new_state = np.copy(board_state)
        new_state[zero_coordinate], new_state[new_position] = new_state[new_position], new_state[zero_coordinate]
        return new_state

    @staticmethod
    def get_available_actions(board_state):        
        zero_pos = Agent.get_zero_coordinate(board_state)
        vertical_actions = (["down"],["up", "down"] ,["up"])
        horizontal_actions = (["right"],["left", "right"] ,["left"])
        x_coordinate = zero_pos[1]       
        y_coordinate = zero_pos[0]
        available_actions = vertical_actions[y_coordinate] + horizontal_actions[x_coordinate]
        return available_actions

    @staticmethod
    def goal_reached(board_state):
        return np.array_equal(board_state, Agent.target_state)
    
    def __init__(self, current_state):
        self.current_state = current_state




class AStarAgent(Agent):
    def __init__(self, current_state):
        super().__init__(current_state)

    def create_plan(self):
        pass
        
    def get_zero_coordinate(board_state):
        return np.array(np.where(board_state==0)).reshape(2)
    
    def heuristic_manhattan(self, board_state):
        h = 0
        #TODO check if the 0 cell manhattan distance should be included
        for i in range(9):                        
            h += np.absolute((np.array(np.where(board_state==i)) - np.array(np.where(self.target_state==i)))).sum()
        return h

    def heuristic_euclidean(self, board_state):
        h = 0
        #TODO check if the 0 cell euclidean distance should be included
        for i in range(9):                        
            h += np.sqrt(np.square((np.array(np.where(board_state==i)) - np.array(np.where(self.target_state==i)))).sum())
        return h





