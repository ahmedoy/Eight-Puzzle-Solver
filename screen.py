import tkinter as tk

class Screen:
    def __init__(self, tile_size, window_height, window_width, allow_keyboard=False):
        self.tile_size = tile_size
        self.window_height = window_height
        self.window_width = window_width
        self.allow_keyboard = allow_keyboard

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height)
        self.canvas.pack()

    def display(self, board_state):
        self.canvas.delete("all")
        
        # Iterate over the board state and display tiles
        for i in range(board_state.shape[0]):
            for j in range(board_state.shape[1]):
                x0 = j * self.tile_size
                y0 = i * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size                
                if board_state[i][j] != 0: 
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="red")
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(board_state[i][j]), fill="black")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")

    def run(self):
        self.window.mainloop()



        