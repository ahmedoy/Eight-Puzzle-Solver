import keyboard
import screen
import board


class Game:
    def __init__(self,  display=False):
        initial_state = [1,2,0,3,4,5,6,7,8]
        self.board = board.Board(initial_state)
        self.display = display
        self.key_responses()
        if display:
            self.create_window()
        self.game_loop()        

    
    def game_loop(self):
        while not self.board.check_win():
            pass
        
        #Add Game Response after winning here
        
    def key_responses(self):
        keyboard.on_press_key("up", self.on_arrow_key)
        keyboard.on_press_key("down", self.on_arrow_key)
        keyboard.on_press_key("left", self.on_arrow_key)
        keyboard.on_press_key("right", self.on_arrow_key)


    def on_arrow_key(self, event):
        controls_dict = {'up':'down', 'down':'up', 'right':'left', 'left':'right'} #inverted controls are easier for the player        
        if self.board.take_action(controls_dict[event.name]) == True:
            self.game_screen.display(self.board.get_state())


    
    def create_window(self):
        tile_size = 60
        window_height = 240
        window_width = 240
        self.game_screen = screen.Screen(tile_size, window_height, window_width)
        self.game_screen.display(self.board.get_state())
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