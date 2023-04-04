import tkinter as tk
import random
from dataclasses import dataclass


@dataclass
class GameOfLife:
    window: object = tk.Tk()
    window.title("Peers Conway's Game of Life")
    grid_height: int = 50
    grid_width: int = 50
    cell_size: int = 10

    def __post_init__(self):
        self.create_widgets()
        self.create_grid()

    def create_widgets(self) -> None:
        """ Creates the widgets for the game of life
        """
        self.canvas = tk.Canvas(self.window, width=self.grid_width * self.cell_size, height=self.grid_height * self.cell_size,
                                borderwidth=1, highlightthickness=1, bg="gray")
        self.canvas.pack(side="top", fill="both", expand="true")

        tk.Button(self.window, text="Start",
                  command=self.start_game).pack(side="left")
        tk.Button(self.window, text="Stop",
                  command=self.stop_game).pack(side="left")
        tk.Button(self.window, text="Reset",
                  command=self.reset_game).pack(side="left")

    def get_grid(self) -> list[list[int]]:
        """ Creates a random grid

        Returns:
            list[list[int]]: A random grid
        """
        return [[random.randint(0, 1) for _ in range(self.grid_width)]  # for each column in the row
                for _ in range(self.grid_height)]  # for each row

    def create_grid(self) -> None:
        """ Creates the grid
        """
        self.grid = self.get_grid()  # get a random grid
        self.draw_grid()  # draw the grid

    def draw_grid(self) -> None:
        """ Draws the grid
        """
        self.canvas.delete("all")  # clear the canvas
        for i in range(self.grid_height):  # for each row
            for j in range(self.grid_width):  # for each column in the row
                x1_cord = j * self.cell_size
                y1_cord = i * self.cell_size
                x2_cord = x1_cord + self.cell_size
                y2_cord = y1_cord + self.cell_size
                if self.grid[i][j] == 1:  # if cell is alive
                    self.canvas.create_rectangle(
                        x1_cord, y1_cord, x2_cord, y2_cord, fill="yellow", outline="")
                else:  # if cell is dead
                    self.canvas.create_rectangle(
                        x1_cord, y1_cord, x2_cord, y2_cord, fill="gray", outline="")

    def get_neighbors(self, i: int, j: int) -> int:
        """ Gets the number of neighbors

        Args:
            i (int): row
            j (int): column

        Returns:
            int: number of neighbors
        """
        neighbors = 0  # number of neighbors
        for x in [-1, 0, 1]:  # for each neighbor in the row
            for y in [-1, 0, 1]:  # for each neighbor in the column
                if x == 0 and y == 0:  # if the cell is itself
                    continue
                if i + x < 0 or i + x >= self.grid_height or j + y < 0 or j + y >= self.grid_width:  # if the cell is out of bounds
                    continue
                if self.grid[i + x][j + y] == 1:  # if the neighbor is alive
                    neighbors += 1  # add 1 to the number of neighbors
        return neighbors

    def update_grid(self) -> None:
        """ Updates the grid
        """
        if self.running == False:  # if the game is not running
            return
        new_grid = self.get_grid()  # create a new grid
        for i in range(self.grid_height):  # for each row
            for j in range(self.grid_width):  # for each column in the row
                # get the number of neighbors
                neighbors = self.get_neighbors(i, j)
                if self.grid[i][j] == 1:  # if the cell is alive
                    if neighbors < 2 or neighbors > 3:  # if the cell has less than 2 or more than 3 neighbors
                        new_grid[i][j] = 0  # the cell dies
                    else:  # if the cell has 2 or 3 neighbors
                        new_grid[i][j] = 1  # the cell lives
                else:  # if the cell is dead
                    if neighbors == 3:  # if the cell has 3 neighbors
                        new_grid[i][j] = 1  # the cell lives
                    else:  # if the cell has less than 3 or more than 3 neighbors
                        new_grid[i][j] = 0  # the cell stays dead
        self.grid = new_grid  # update the grid
        self.draw_grid()  # draw the grid
        # call the update_grid function after 100 milliseconds
        self.window.after(100, self.update_grid)

    def start_game(self) -> None:
        """ Starts the game
        """
        self.running = True
        self.update_grid()

    def stop_game(self) -> None:
        """ Stops the game
        """
        self.running = False

    def reset_game(self) -> None:
        """ Resets the game
        """
        self.stop_game()
        self.create_grid()


if __name__ == "__main__":
    game = GameOfLife()
    game.window.mainloop()
