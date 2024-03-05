import numpy as np
import heapdict
from solution import Node

# Base Class for Agents to inherit from
class Agent:
    action_dict = {'up': np.array([-1, 0]), 'down': np.array([1, 0]),
                   'right': np.array([0, 1]), 'left': np.array([0, -1])}
    target_state = np.arange(9).reshape(3, 3)

    @staticmethod
    def is_valid_position(pos):
        return np.all(pos >= 0) and np.all(pos < 3)

    @staticmethod
    def get_zero_coordinate(board_state):
        return np.array(np.where(board_state == 0)).reshape(2)

    @staticmethod
    def execute_action(board_state, action):
        coordinate_change = Agent.action_dict[action]
        zero_coordinate = Agent.get_zero_coordinate(board_state)
        new_position = coordinate_change + zero_coordinate
        zero_coordinate = tuple(zero_coordinate)
        new_position = tuple(new_position)
        new_state = np.copy(board_state)
        new_state[zero_coordinate], new_state[new_position] = new_state[new_position], new_state[zero_coordinate]
        return new_state

    @staticmethod
    def get_available_actions(board_state):
        zero_pos = Agent.get_zero_coordinate(board_state)
        vertical_actions = (["down"], ["up", "down"], ["up"])
        horizontal_actions = (["right"], ["left", "right"], ["left"])
        x_coordinate = zero_pos[1]
        y_coordinate = zero_pos[0]
        available_actions = vertical_actions[y_coordinate] + \
            horizontal_actions[x_coordinate]
        return available_actions

    @staticmethod
    def get_next_states(board_state):
        return [(action, Agent.execute_action(board_state, action)) for action in Agent.get_available_actions(board_state)]

    @staticmethod
    def goal_reached(board_state):
        return np.array_equal(board_state, Agent.target_state)

    @staticmethod
    def get_action_plan(goal_node):
        current_node = goal_node
        action_plan = []
        while current_node.parent != None:  # Traverse the tree upwards, through the parent pointers and add actions to plan
            action_plan.append(current_node.action)
            current_node = current_node.parent
        action_plan.reverse()
        return action_plan
    @staticmethod
    def isSolvable(board_state):
        inv_count = 0
        for i in range(9):
            for j in range(i+1, 9):
                if board_state[j] and board_state[i] and board_state[i] > board_state[j]:
                    inv_count += 1
        return inv_count % 2 == 0
    
    def __init__(self, current_state):
        self.current_state = current_state


class AStarAgent(Agent):
    def __init__(self, current_state):
        super().__init__(current_state)

    def solve(self, manhattan_flag=True):
        explored_states = set()
        priority_queue = heapdict.heapdict() # Insert initial state with no parents in priority queue
        initial_node = Node(board_state=self.current_state, action=None, cost=0, parent=None)
        priority_queue[initial_node] = 0
        goal_node = None #Will be set to the final goal node if puzzle solved successfully

        while len(priority_queue) > 0:
            (chosen_node, priority) = priority_queue.popitem()

            if self.goal_reached(chosen_node.board_state):
                goal_node = chosen_node
                break

            explored_states.add(tuple(chosen_node.board_state.flatten()))
            next_states = self.get_next_states(chosen_node.board_state)

            for action, state in next_states:  # Iterate over next states and actions that lead to them
                temp_node = Node(board_state=state, action=action, cost=1+chosen_node.cost, parent=chosen_node)
                if (tuple(state.flatten()) not in explored_states) and (temp_node not in priority_queue):
                    heuristic = self.get_heuristic(state, manhattan_flag)
                    priority_queue[temp_node] = temp_node.cost + heuristic
                    
                if temp_node in priority_queue: #Decrease Key
                    heuristic = self.get_heuristic(state, manhattan_flag)
                    if temp_node.cost + heuristic < priority_queue[temp_node]:
                        priority_queue[temp_node] = temp_node.cost + heuristic

        if goal_node:  # if a solution was found, build the action plan
            return self.get_action_plan(goal_node)
        else:
            return False  # Solution Not Found (empty action plan)

    def get_heuristic(self, board_state, manhattan_flag=True):
        if manhattan_flag:
            return self.heuristic_manhattan(board_state)
        else:
            return self.heuristic_euclidean(board_state)

    def heuristic_manhattan(self, board_state):
        h = 0
        # TODO check if the 0 cell manhattan distance should be included
        for i in range(1, 9):
            h += np.absolute((np.array(np.where(board_state == i)) -
                             np.array(np.where(self.target_state == i)))).sum()
        return h

    def heuristic_euclidean(self, board_state):
        h = 0
        # TODO check if the 0 cell euclidean distance should be included
        for i in range(1, 9):
            h += np.sqrt(np.square((np.array(np.where(board_state == i)) -
                         np.array(np.where(self.target_state == i)))).sum())
        return h
class BFSAgent(Agent):

    def __init__(self, current_state):
        super().__init__(current_state)

    def solve (self):
        explored_states = set()
        # make a queue of nodes to visit
        queue = []
        # Insert initial state with no parents in queue
        initial_node = Node(board_state=self.current_state, action=None, cost=0, parent=None)
        # if not self.isSolvable(initial_node.board_state):
        #     return False
        
        queue.append(initial_node)
        goal_node = None

        while len(queue) > 0:
            chosen_node = queue.pop(0)

            if self.goal_reached(chosen_node.board_state):
                goal_node = chosen_node
                break

            explored_states.add(tuple(chosen_node.board_state.flatten()))
            next_states = self.get_next_states(chosen_node.board_state)

            for action, state in next_states:
                temp_node = Node(board_state=state, action=action, cost=1+chosen_node.cost, parent=chosen_node)
                if tuple(state.flatten()) not in explored_states and temp_node not in queue:
                    queue.append(temp_node)
                    explored_states.add(tuple(state.flatten()))

        if goal_node:
            return self.get_action_plan(goal_node)
        else:
            return False
        
