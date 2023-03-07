import pickle
from time import time
from src.logic.puzzle import Puzzle


class IDAStar:
    def __init__(self, puzzle):
        """Intializes the IDA* algorithm heuristics, from the file with patterns & their weights.
        """
        self.puzzle = puzzle
        try:
            with open("patterns.dat", "rb") as file:
                self.groups = pickle.load(file)
                self.patterns = pickle.load(file)
                if sum(len(group) for group in self.groups) != self.puzzle.size ** 2 - 1:
                    self.status = (
                    "Cannot solve the Puzzle, because additive pattern database" +
                    " does not match with this Puzzle")
                    self.groups = None
                else:
                    self.status = ("The algorithm uses the additive pattern" +
                          " database for heuristics, with the groupings of " +
                          f"({', '.join(str(len(group)) for group in self.groups)})")
        except FileNotFoundError:
            self.status = "Missing 'patterns.dat' file, try to rebuild the pattern database"
            self.groups = None
        self.count = 0
    
    def start(self):
        """Initializes algorithm's starting position and data structures if groups have been 
        assigned. Then iterates with new bound values until Puzzle is solved.

        Returns:
            list: List of directions to solve the Puzzle.
        """
        if not self.groups:
            return False
        start = time()
        bound = self.heuristic(self.puzzle)
        path, directions = [self.puzzle], []
        while True:
            t = self.search(path, directions, 0, bound)
            if t is True:
                print(f"Visited {self.count} nodes.")
                return directions, round(time() - start, 2)
            bound = t

    def search(self, path: list, directions: list, g: int, bound: int):
        """Uses IDA* to recursively find the optimal path to the goal state. Calculates 'f' 
        value for the last puzzle in the path. Backtracks if 'f' value exceeds the given 
        bound. Updates the bound if all directions exceed it. Terminates recursion and 
        returns True when goal state is reached.

        Args:
        path (list): A list of Puzzles representing the current path.
        directions (list): A list of directions taken to reach the current state.
        g (int): The moves used to reach the current state from the initial state.
        bound (int): The maximum value of moves to reach the goal state.

    Returns:
        bool: If the goal state is reached, returns True.
        min_bound: Otherwise, returns the minimum possible bound for the path.
    """
        puzzle: Puzzle = path[-1]
        f = g + self.heuristic(puzzle)
        if f > bound:
            return f
        if puzzle.is_solved():
            return True
        min_bound = float('inf')
        for direction in puzzle.directions:
            if directions and [-direction[0], -direction[1]] == directions[-1]:
                continue
            simulated = puzzle.simulate(direction)
            if not simulated or simulated in path:
                continue
            path.append(simulated)
            directions.append(direction)
            t = self.search(path, directions, g + 1, bound)
            if t is True:
                return True
            min_bound = min(min_bound, t)
            path.pop()
            directions.pop()
        return min_bound

    def heuristic(self, puzzle: Puzzle):
        """Calculates the total bound for the given Puzzle, sum of the groups bound values.

        Args:
            puzzle (Puzzle): The Puzzle to be calculated.

        Returns:
            bound: The moves needed to get into solved state from this Puzzle.
        """
        self.count += 1
        bound = 0
        for i, group in enumerate(self.groups):
            hashed_puzzle = puzzle.hash(group)
            bound += self.patterns[i][hashed_puzzle]
        return bound
