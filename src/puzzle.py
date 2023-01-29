from random import randrange


class Puzzle:
    """Object representing the puzzle."""

    def __init__(self, size = 4):
        """Initializes a new puzzle using 2-dimensional array, setting their numbers and shuffling the numbers."""
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.position = [self.size - 1, self.size - 1]
        self.moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def set_numbers(self):
        """Sets the numbers to the board, and leaves blank space at the end for the game.
        """
        for x in range(self.size):
            for y in range(self.size):
                self.board[x][y] = (x * self.size) + (y + 1)
        self.board[self.position[0]][self.position[1]] = ""

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
        """Moves a number from some direction to the blank position.

        Args:
            direction (list): x and y coordinates to move to
        """
        new_position = [self.position[0] + direction[0],
                        self.position[1] + direction[1]]
        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= self.size or new_position[1] >= self.size:
            return
        self.board[self.position[0]][self.position[1]] = self.board[new_position[0]][new_position[1]]
        self.board[new_position[0]][new_position[1]] = ""
        self.position = new_position

    def shuffle_board(self, times: int):
        """Shuffles the board by moving pieces in random order.

        Args:
            times (int): how many times to move the pieces
        """
        for i in range(times):
            self.move_number(self.moves[randrange(4)])
