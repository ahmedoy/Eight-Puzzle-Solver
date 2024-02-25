import numpy as np

class Board:
    @staticmethod
    def is_valid_position(pos):
        return np.all(pos >= 0) and np.all(pos < 3)
    
    def __init__(self, initial_state = None):
        #initial_state should be a python list of numbers from 0 to 8 arranged in any order
        if initial_state:
            self.arr = np.array(initial_state, dtype=np.int8).reshape(3,3)
        else:
            #random initialization
            self.arr = np.arange(9)
            np.random.shuffle(self.arr)
            self.arr = self.arr.reshape(3,3)

        #Action Dictionary defining the change in coordinates (x,y) for each action
        self.action_dict = {'up':np.array([-1,0]), 'down':np.array([1,0]), 'right':np.array([0,1]), 'left':np.array([0,-1]) }

        self.target_state = np.arange(9).reshape(3,3)
    

    def validate_state(self):
        #TODO handle invalid initial states 
        pass

    def check_win(self):
        return self.arr == self.target_state

    def get_state(self):
        return self.arr
    
    def take_action(self, action):
        if action not in self.action_dict.keys():
            raise Exception("Invalid Action: Only use up, down, left, and right")
        
        coordinate_change = self.action_dict[action]
        zero_coordinate =   self.get_zero_coordinate() 
        new_position = coordinate_change + zero_coordinate
        
        if self.is_valid_position(new_position):
            zero_coordinate = tuple(zero_coordinate)
            new_position = tuple(new_position)
            self.arr[zero_coordinate], self.arr[new_position] = self.arr[new_position], self.arr[zero_coordinate]
        else:
            print("Action not taken")

 
    def get_zero_coordinate(self):
        return np.array(np.where(self.arr==0)).reshape(2)