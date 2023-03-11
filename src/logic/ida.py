import pickle
from time import time
from src.logic.puzzle import Puzzle


class IDAStar:
    def __init__(self, puzzle: Puzzle):
        """Intializes the IDA* algorithm heuristics, from the file with patterns & their weights.
        """
        self.puzzle = puzzle
        try:
            with open("patterns.dat", "rb") as file:
                self.groups, self.patterns = pickle.load(
                    file), pickle.load(file)
                if sum(len(g) for g in self.groups) != self.puzzle.size ** 2 - 1:
                    self.status, self.groups = "Cannot solve due to pattern database mismatch", None
                else:
                    self.status = "Using pattern database for heuristics with groupings of "\
                        + f"({', '.join(str(len(g)) for g in self.groups)})"
        except FileNotFoundError:
            self.status, self.groups = "Missing 'patterns.dat' file, rebuild the pattern database",\
                None

    def start(self):
        """Initializes algorithms starting position and data structures if groups have been
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
                return directions, round(time() - start, 2)
            bound = t

    def search(self, path: list, directions: list, g: int, bound: int):
        """This function uses IDA* to find the optimal path to the goal state. It calculates 'f'
        for the last puzzle in the path, backtracks if 'f' exceeds the bound, and updates the bound
        if all directions exceed it. It returns True when the goal state is reached or the minimum
        bound for the path otherwise.

        Args: path (a list of Puzzles), directions (a list of directions),
        g (the moves used to reach the current state), and bound (the max moves to reach the goal).

        Returns: True if goal reached, otherwise the minimum bound for the path.
    """
        current: Puzzle = path[-1]
        f = g + self.heuristic(current)
        if f > bound:
            return f
        if current.is_solved():
            return True
        min_bound = float('inf')
        for direction in current.directions:
            if directions and [-direction[0], -direction[1]] == directions[-1]:
                continue
            simulated = current.simulate(direction)
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

    def heuristic(self, current: Puzzle):
        """Calculates the total bound for the given Puzzle, sum of the groups bound values.

        Args:
            puzzle (Puzzle): The Puzzle to be calculated.

        Returns:
            bound: The moves needed to get into solved state from this Puzzle.
        """
        bound = 0
        for i, group in enumerate(self.groups):
            hashed_puzzle = current.hash(group)
            bound += self.patterns[i][hashed_puzzle]
        return bound
