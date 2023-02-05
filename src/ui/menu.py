import tkinter as tk
from tkinter import Button
from static.style import BACKGROUND_COLOR, NORMAL_FONT, BIG_FONT, MOVES_FONT


class Menu(tk.Frame):
    """
    A class that represents the menu bar in the GUI window of the 15-puzzle game solver.
    """

    def __init__(self, width, height, master):
        """
        Initializes the Menu component of the GUI.

        Args:
        width (int): The width of the menu bar.
        height (int): The height of the menu bar.
        master (Tk): The parent window of the menu bar.

    """
        tk.Frame.__init__(self)
        self.height = height
        self.master = master
        self.frame = tk.Frame(
            master, bg=BACKGROUND_COLOR, bd=3, width=width, height=height)
        self.width = width / 5
        self.frame.grid()

    def draw_button(self, col, name, com):
        """
        Draws a button in the menu bar.

        Args:
            col (int): The column where the button should be placed in the menu bar.
            name (str): The text label of the button.
            com (function): The function to be executed when the button is clicked.

        """
        frame = tk.Frame(
            self.frame,
            bg=BACKGROUND_COLOR,
            width=int(self.width),
            height=self.height)
        frame.grid(row=0, column=col, padx=1, pady=1)
        button = Button(self.frame, text=name,
                        highlightbackground=BACKGROUND_COLOR, font=NORMAL_FONT, command=com)
        button.grid(column=col, row=0, rowspan=2)

    def draw_moves(self, col):
        """
        Draws the moves count in the menu bar.

        Args:
            col (int): The column where the moves counter should be placed in the menu bar.

        """
        frame = tk.Frame(self.frame, bg=BACKGROUND_COLOR,
                         width=self.width, height=self.height)
        frame.grid(row=0, column=col, padx=0, pady=0)
        tk.Label(self.frame, text="Moves", font=BIG_FONT,
                 bg=BACKGROUND_COLOR).grid(column=col, row=0)
        self.moves_label = tk.Label(self.frame, text="0",
                                    font=MOVES_FONT, bg=BACKGROUND_COLOR)
        self.moves_label.grid(column=col, row=1)

    def update_moves(self, moves):
        """
        Updates the moves count displayed in the menu bar.

        Args:
            moves (int): The new count of moves.

        """
        self.moves_label.configure(text=moves)
