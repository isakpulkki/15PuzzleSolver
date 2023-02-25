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
                    print(
                        "Cannot perform IDA* to solve the Puzzle, because additive pattern database" +
                        " does not match with this Puzzle.")
                    self.groups = None
                else:
                    print("To solve the Puzzle, IDA* algorithm will use the additive pattern" +
                          " database for heuristics, with the groupings of " +
                          f"({', '.join(str(len(group)) for group in self.groups)}).")
        except FileNotFoundError:
            print("No 'patterns.dat' found, try to rebuild the pattern database.")
            self.groups = None

    def start(self):
        """If the groups have been assigned, initializes the starting position of the algorithm,
        and the required data structures. Then, until the Puzzle is solved, the algorithm will
        iterate with the new bound values found.

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
                print(
                    f"The algorithm found the path in {round(time() - start, 2)} seconds.")
                return directions
            bound = t

    def search(self, path: list, directions: list, g: int, bound: int):
        """Recursively finds the optimal path to the goal state using IDA* (Iterative Deepening A*)
        algorithm. The algorithm takes the last puzzle in the path and calculates its 'f' value
        (moves + heuristic).
        If this value exceeds the given bound, the algorithm backtracks and returns the minimum
        possible bound from this path.
        If all the directions exceed the bound, the bound is updated and the search is repeated
        with the new bound. If the goal state is reached, the recursion terminates and returns True.

        Args:
        path (list): A list of Puzzles representing the current path.
        directions (list): A list of directions taken to reach the current state
        from the previous states.
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
        bound = 0
        for i, group in enumerate(self.groups):
            hashed_puzzle = puzzle.hash(group)
            bound += self.patterns[i][hashed_puzzle]
        return bound
