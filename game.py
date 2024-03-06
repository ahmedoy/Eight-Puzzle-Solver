import keyboard
import screen
import board
import agents


class Game:
    def __init__(self,  display=False):
        initial_state = [1,2,0,3,4,5,6,7,8]
        self.board = board.Board(initial_state)
        if not self.board.is_solvable():
            print("Insolvable State. Quitting Game")
            return
        self.display = display
        self.agent = agents.AStarAgent(self.board.get_state())
        self.agent= agents.BFSAgent(self.board.get_state())
        self.expanded_nodes, self.action_plan = self.agent.solve() #TODO handle if no solution found (empty action plan list)
        self.action_idx = 0   
        self.key_responses()
        if display:
            print("Creating Window")
            self.create_window()
        self.game_loop()        

    
    def game_loop(self):
        while not self.board.check_win():
            pass
        
        #TODO Add Game Response after winning here
        
    def key_responses(self):
        keyboard.on_press_key("left", self.on_arrow_key)
        keyboard.on_press_key("right", self.on_arrow_key)


    def on_arrow_key(self, event):
        inverted_controls = {'up':'down', 'down':'up', 'right':'left', 'left':'right'} #inverted controls for replaying action plan backwards
        if event.name == 'right' and self.action_idx < len(self.action_plan):
            #print(f"action plan = {self.action_plan[self.action_idx]}")
            self.board.take_action(self.action_plan[self.action_idx])
            #print(f"expanded nodes = {self.expanded_nodes[self.action_idx]}")
            #self.expanded_nodes_board.take_action(self.expanded_nodes[self.action_idx])
            self.action_idx +=1
            self.game_screen.display(self.board.get_state(), self.expanded_nodes[self.action_idx])
        elif event.name =='right' and self.action_idx < len(self.expanded_nodes) - 1:
            #self.expanded_nodes_board.take_action(self.expanded_nodes[self.action_idx])
            self.action_idx +=1
            self.game_screen.display(self.board.get_state(), self.expanded_nodes[self.action_idx])
        elif event.name == 'left' and self.action_idx > 0 and (self.action_idx < len(self.action_plan) or self.action_idx < len(self.action_plan)):
            self.action_idx -= 1
            self.board.take_action(inverted_controls[self.action_plan[self.action_idx]])
            #self.expanded_nodes_board.take_action(inverted_controls[self.expanded_nodes[self.action_idx]])
            self.game_screen.display(self.board.get_state(), self.expanded_nodes[self.action_idx])
        elif event.name == 'left' and self.action_idx > 0 and self.action_idx < len(self.expanded_nodes):
            self.action_idx -= 1
            #self.expanded_nodes_board.take_action(inverted_controls[self.expanded_nodes[self.action_idx]])
            self.game_screen.display(self.board.get_state(), self.expanded_nodes[self.action_idx])
        

    
    def create_window(self):
        tile_size = 80
        window_height = 500
        window_width = 300
        self.game_screen = screen.Screen(tile_size, window_height, window_width)
        self.game_screen.display(self.board.get_state(), self.board.get_state())
        self.game_screen.run()          

        







if __name__ == '__main__':
    Game(display=True)
    




# # Example usage:
# tile_size = 60
# window_height = 240
# window_width = 240
# board_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Example board state
# game_screen = Screen(tile_size, window_height, window_width)
# game_screen.display(board_state)
# game_screen.run()    