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
    

    def check_win(self):        
        return np.array_equal(self.arr, self.target_state)

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
            return True
        else:
            print("Action not taken")
            return False

 
    def get_zero_coordinate(self):
        return np.array(np.where(self.arr==0)).reshape(2)
    

    def is_solvable(self):
        solvable = True
        arr_1d = self.arr.reshape(-1)
        for i in range(arr_1d.shape[0]-1):
            for j in range(i+1, arr_1d.shape[0]):
                if arr_1d[j] < arr_1d[i]:
                    solvable = not solvable

        return solvable
