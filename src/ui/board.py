import tkinter as tk
from src.logic.puzzle import Puzzle
from src.static.style import BLACK, ITALIC, GRAY


class Board(tk.Frame):
    """This class is responsible for creating and updating the game board for the 15 puzzle game.
    """

    def __init__(self, width: int, master):
        """Initializes the Board class.
        Args:
            width (int): Width of the board.
            master (Application): The parent widget."""

        tk.Frame.__init__(self)
        self.master = master
        self.board = tk.Frame(
            self.master, bg=BLACK, bd=3, width=width, height=width)
        self.board.grid()
        self.width = width
        self.cells = []

    def init_board(self, puzzle: Puzzle):
        """Initialize the cells in the board.
        Args:
            puzzle (Puzzle): The puzzle object containing information about each piece."""
        piece_width = self.width / puzzle.size
        for x in range(puzzle.size):
            row = []
            for y in range(puzzle.size):
                number = puzzle[x][y]
                if number == 0:
                    number = ""
                background = GRAY if number else BLACK
                frame = tk.Frame(self.board, bg=background,
                                 width=piece_width, height=piece_width)
                frame.grid(row=x, column=y, padx=1, pady=1)
                frame.bind("<ButtonRelease-1>", self.on_click)
                cell_number = tk.Label(self.board,
                                       text=number, bg=background, font=ITALIC)
                cell_number.grid(row=x, column=y)
                cell_number.bind("<ButtonRelease-1>", self.on_click)
                cell_data = {"frame": frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

    def update_piece(self, x: int, y: int, number: int, color: str):
        """Update the background color and number of a cell.
        Args:
            x (int): X-coordinate of the cell to update.
            y (int): Y-coordinate of the cell to update.
            number (int): The new number to set for the cell.
            color (str): The wanted color of the number.
        """
        if number == 0:
            number = ""
        background = GRAY if number else BLACK
        self.cells[x][y]["frame"].configure(bg=background)
        self.cells[x][y]["number"].configure(
            bg=background, text=number, fg=color)

    def on_click(self, event):
        """Handle a click event on a cell.
        Args:
            event (tk.Event): The click event."""
        row = event.widget.grid_info().get("row")
        column = event.widget.grid_info().get("column")
        self.master.update_number(row, column)
