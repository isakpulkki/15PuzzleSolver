import tkinter as tk
from ui.menu import Menu
from ui.board import Board
from logic.puzzle import Puzzle


class Application(tk.Tk):
    """
    A class that represents a GUI layer for solving the 15-puzzle game using search algorithms.
    It creates the GUI window and displays the puzzle board and the menu bar.
    """

    def __init__(self):
        """
        Initializes the Tkinter window, creates an instance of the Puzzle class, sets the puzzle numbers,
        shuffles the board, creates instances of the Menu and Board classes etc.
        """
        tk.Tk.__init__(self)
        self.iconphoto(False, tk.PhotoImage(file='src/static/puzzle.png'))
        self.title('15PuzzleSolver')
        puzzle = Puzzle()
        puzzle.set_numbers()
        puzzle.shuffle_board(999)
        self.puzzle = puzzle
        self.grid()
        self.width = 650
        self.menu = Menu(self.width, 40, self)
        self.init_menu()
        self.board = Board(self.width, self)
        self.board.init_board(self.puzzle)
        self.moves = 0
        self.mainloop()

    def init_menu(self):
        """
        Draws the buttons and the moves label on the menu bar.
        """
        self.menu.draw_button(0, "Shuffle", lambda: [self.puzzle.shuffle_board(
            999), self.reset_moves(), self.update()])
        self.menu.draw_button(1, "Help", None)
        self.menu.draw_moves(2)
        self.menu.draw_button(3, "Solve", None)
        self.menu.draw_button(4, "Exit", self.destroy)

    def reset_moves(self):
        """
        Resets the number of moves to 0.
        """
        self.moves = 0

    def update_number(self, x, y):
        """
        Attempts to move the number at the given positionition (x, y) in the puzzle and updates the number of moves.
        Args:
            x (int): x-coordinate of the number to be moved.
            y (int): y-coordinate of the number to be moved.
        """
        direction = [x - self.puzzle.position[0],
                     y - self.puzzle.position[1]]
        if self.puzzle.move_number(direction):
            self.moves += 1
        self.update()

    def update(self):
        """
        Updates the number of moves displayed on the menu bar and the state of the puzzle board.
        """
        self.menu.update_moves(self.moves)
        for x in range(self.puzzle.size):
            for y in range(self.puzzle.size):
                number = self.puzzle.get_number(x, y)
                self.board.update_piece(x, y, number)


if __name__ == "__main__":
    Application()
