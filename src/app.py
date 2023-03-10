import tkinter as tk
from src.ui.menu import Menu
from src.ui.board import Board
from src.logic.puzzle import Puzzle
from src.logic.ida import IDAStar
from src.static.style import WHITE, GREEN, BLACK
from src.ui.footer import Footer


class Application(tk.Tk):
    """
    A class that represents a GUI layer for solving the 15-puzzle game using search algorithms.
    It creates the GUI window and displays the puzzle board and the menu bar.
    """

    def __init__(self):
        """
        Initializes the Tkinter window, creates an instance of Puzzle class, sets puzzle numbers,
        shuffles the board, creates instances of the Menu and Board classes etc.
        """
        tk.Tk.__init__(self)
        print("Welcome to 15PuzzleSolver!")
        self.iconphoto(False, tk.PhotoImage(file='src/static/puzzle.png'))
        self.title('15PuzzleSolver')
        self.resizable(False, False)
        self.configure(background=BLACK)
        self.puzzle = Puzzle(4)
        self.puzzle.set_numbers()
        self.puzzle.shuffle_board(999)
        self.width = 600
        self.moves = 0
        self.menu = Menu(self.width, 40, self)
        self.idastar = IDAStar(self.puzzle)
        self.board = Board(self.width, self)
        self.footer = Footer(self.width, self)
        self.make_gui()
        self.mainloop()

    def make_gui(self):
        """
        Draws the buttons and the moves label on the menu bar.
        """
        self.grid()
        self.menu.draw_moves(2)
        self.menu.draw_button(3, "Solve", self.solve)
        self.board.init_board(self.puzzle)
        if not self.idastar.groups:
            self.menu.switch_buttons()
        self.menu.draw_button(1, "Shuffle", lambda: [self.puzzle.shuffle_board(
            999), self.reset_moves(), self.update()])
        self.footer.set_text(self.idastar.status)

    def reset_moves(self):
        """
        Resets the number of moves to 0.
        """
        self.puzzle.moves = 0

    def update_number(self, x: int, y: int):
        """
        Attempts to move the number at the given positionition (x, y)
        in the puzzle and updates the number of moves.
        Args:
            x (int): x-coordinate of the number to be moved.
            y (int): y-coordinate of the number to be moved.
        """
        direction = [x - self.puzzle.position[0],
                     y - self.puzzle.position[1]]
        if direction in self.puzzle.directions:
            self.puzzle.move_number(direction)
            self.puzzle.moves += 1
        self.update()

    def solve(self):
        """
        Solves the current Puzzle with IDA* algorithm.
        """
        self.idastar.puzzle = self.puzzle
        directions, time = self.idastar.start()
        if directions:
            self.footer.set_text(
                f"Found the path in {time} seconds".replace(".", ","))
            self.menu.switch_buttons()
            var = tk.IntVar(self)
            for direction in directions:
                self.puzzle.move_number(direction)
                self.puzzle.moves += 1
                self.update()
                self.after(350, var.set, 1)
                self.wait_variable(var)
            self.menu.switch_buttons()

    def update(self):
        """
        Updates the number of moves displayed on the menu bar and the state of the puzzle board.
        """
        color = WHITE
        self.menu.update_moves(self.puzzle.moves)
        if self.puzzle.is_solved():
            self.reset_moves()
            color = GREEN
        for x in range(self.puzzle.size):
            for y in range(self.puzzle.size):
                number = self.puzzle[x][y]
                self.board.update_piece(x, y, number, color)


if __name__ == "__main__":
    Application()
