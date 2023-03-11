from copy import deepcopy
from random import randrange


class Puzzle:
    """Object representing the Puzzle."""

    def __init__(self, size):
        """Initializes a new puzzle using 2-dimensional array, setting their numbers and shuffling
        the numbers."""
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.position = [self.size - 1, self.size - 1]
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.moves = 0

    def set_numbers(self):
        """Sets the numbers to the board, and leaves blank space at the end for the game.
        """
        self.board = [[(x * self.size) + (y + 1)
                       for y in range(self.size)] for x in range(self.size)]
        self.board[self.position[0]][self.position[1]] = 0

    def move_number(self, direction: list):
        """Moves a number from some direction to the blank position.
        Args:
            direction (list): x and y coordinates to move to
        """
        new_x, new_y = self.position[0] + \
            direction[0], self.position[1] + direction[1]
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            self.board[self.position[0]][self.position[1]
                                         ] = self.board[new_x][new_y]
            self.board[new_x][new_y] = 0
            self.position = [new_x, new_y]
            return True
        return False

    def shuffle_board(self, times: int):
        """Shuffles the board by moving pieces in random order.
        Args:
            times (int): How many times to move the pieces.
        """
        for _ in range(times):
            self.move_number(self.directions[randrange(4)])

    def hash(self, group):
        """This is the hash function for the pattern builder, to give each permutation
        unique hash to keep count of the visited nodes.
        Args:
            group (dict): This is the group of numbers which will be included in the hash.
        Returns:
            str: The hash as a String.
        """
        puzzle_hash = [""]*2*(self.size**2)

        for i in range(self.size):
            for j in range(self.size):
                if self[i][j] in group:
                    puzzle_hash[2*self[i][j]] = str(i)
                    puzzle_hash[2*self[i][j]+1] = str(j)
        return "".join(puzzle_hash)

    def simulate(self, direction: list):
        """This will generate a new Puzzle, and move the blank square to a new position,
        giving us a new permutation.
        Args:
            direction (list): Coordinates of the direction the blank square should move to.
        Returns:
            Puzzle: The copied Puzzle with move made.
        """

        puzzle_copy = deepcopy(self)
        return puzzle_copy if puzzle_copy.move_number(direction) else False

    def is_solved(self):
        """Checks if the Puzzle has been solved.
        Returns:
            bool: True if solved.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] not in [i * self.size + j + 1, 0]:
                    return False
        return True

    def __getitem__(self, key):
        return self.board[key]
