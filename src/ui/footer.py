import tkinter as tk
from src.static.style import BLACK, WHITE, SMALL


class Footer(tk.Frame):
    """
    A class that represents the Info bar in the bottom of the GUI window.
    """

    def __init__(self, width: int, master):
        """
        Initializes the Info component of the GUI.
        Args:
            width (int): The width of the Info bar.
            master (Tk): The parent window of the Info bar.
    """
        tk.Frame.__init__(self)
        self.width = width
        self.master = master
        self.frame = tk.Frame(
            master, bg=BLACK, bd=3, width=width)
        self.frame.grid()
        self.label = tk.Label(self.frame, text="",
                              font=SMALL, bg=BLACK, fg=WHITE)
        self.label.grid()

    def set_text(self, x):
        self.label.configure(text=x)
