import tkinter as tk

class Screen:
    def __init__(self, tile_size, window_height, window_width, allow_keyboard=False):
        self.tile_size = tile_size
        self.window_height = window_height
        self.window_width = window_width    
        self.allow_keyboard = allow_keyboard

        self.window = tk.Tk()
        self.solution_canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height)
        self.expanded_nodes_canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height)
        self.path_label = tk.Label(self.window, text="Path Nodes", font=('calibre',10,'bold'))
        self.expanded_nodes_label = tk.Label(self.window, text="Expanded Nodes", font=('calibre',10,'bold'))
        self.solution_canvas.grid(row=0, column=0)
        self.expanded_nodes_canvas.grid(row=0, column=1)
        self.path_label.grid(row=1, column=0)
        self.expanded_nodes_label.grid(row=1, column=1)
    
        
    def display(self, board_state, nodes_expanded):
        self.solution_canvas.delete("all")
        self.expanded_nodes_canvas.delete("all")
        self.canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height)
        self.window.title("8-Puzzle Game")
        self.canvas.pack()

    def display(self, board_state,nodes_expanded):
        self.canvas.delete("all")
        
        # Iterate over the board state and display tiles
        for i in range(board_state.shape[0]):
            for j in range(board_state.shape[1]):
                x0 = j * self.tile_size
                y0 = i * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size                
                if board_state[i][j] != 0: 
                    self.solution_canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="red")
                    self.solution_canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(board_state[i][j]), fill="black")
                else:
                    self.solution_canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")
        # Iterate over the expanded nodes and display tiles
        for i in range(nodes_expanded.shape[0]):
            for j in range(nodes_expanded.shape[1]):
                x0 = j * self.tile_size
                y0 = i * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size                
                if nodes_expanded[i][j] != 0: 
                    self.expanded_nodes_canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="blue")
                    self.expanded_nodes_canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(nodes_expanded[i][j]), fill="black")
                else:
                    self.expanded_nodes_canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")

    def run(self):
        self.window.mainloop()



        