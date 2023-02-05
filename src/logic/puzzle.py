from random import randrange


class Puzzle:
    """Object representing the puzzle."""

    def __init__(self, size=4):
        """Initializes a new puzzle using 2-dimensional array, setting their numbers and shuffling the numbers."""
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.pos = [self.size - 1, self.size - 1]
        self.moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def set_numbers(self):
        """Sets the numbers to the board, and leaves blank space at the end for the game.
        """
        for x in range(self.size):
            for y in range(self.size):
                self.board[x][y] = (x * self.size) + (y + 1)
        self.board[self.pos[0]][self.pos[1]] = ""

    def get_number(self, x: int, y: int):
        """Get a number from a location in the board.

        Args:
            x (int): x-coordinate of the board
            y (int): y-coordinate of the board

        Returns:
            int: the number from the location
        """
        return self.board[x][y]

    def move_number(self, direction: list):
        """Moves a number from some direction to the blank pos.

        Args:
            direction (list): x and y coordinates to move to
        """
        if direction in self.moves:
            new_pos = [self.pos[0] + direction[0],
                       self.pos[1] + direction[1]]
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= self.size or new_pos[1] >= self.size:
                return False
            self.board[self.pos[0]][self.pos[1]
                                    ] = self.board[new_pos[0]][new_pos[1]]
            self.board[new_pos[0]][new_pos[1]] = ""
            self.pos = new_pos
            return True
        return False

    def shuffle_board(self, times: int):
        """Shuffles the board by moving pieces in random order.

        Args:
            times (int): how many times to move the pieces
        """
        for i in range(times):
            self.move_number(self.moves[randrange(4)])
