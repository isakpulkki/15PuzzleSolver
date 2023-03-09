import pickle
from collections import deque
from multiprocessing import Pool
from src.logic.puzzle import Puzzle
import time


class PatternBuilder():
    def __init__(self,  group: dict, size: int):
        """Intializes the pattern database builder with Puzzle, sets it numbers without shuffling.
        Sets moves from the starting position to 0, and initializes a new group with the blank tile.

        Args:
            group (dict): the group of numbers of the Puzzle included in this pattern.
        """
        self.puzzle = Puzzle(size)
        self.puzzle.set_numbers()
        self.puzzle.moves = 0
        self.group = group
        self.blank_group = group.copy()
        self.blank_group.add(0)
        self.iterations = 0

    def build_patterns(self):
        """Applies BFS to all permutations of the Puzzle within the group, starting from 
        the solved state. Uses a queue to store each permutation and its previous direction. 
        Checks for previously visited permutations and adds new ones only if the moved piece 
        is in the group and the other moves are in the same group.

        Returns:
            dict: This is the closed list with all of the permutations of the group.
        """

        visited_list = set()
        closed_list = {}
        open_list = deque()
        open_list.append((self.puzzle, None))
        start = time.time()

        while open_list:
            puzzle, previous = open_list.popleft()
            if self.visit(puzzle, visited_list, closed_list,):
                for direction in self.puzzle.directions:
                    if direction != previous:
                        simulated = puzzle.simulate(direction)
                        if not simulated:
                            continue
                        if simulated[puzzle.position[0]][puzzle.position[1]] in self.group:
                            simulated.moves = puzzle.moves + 1
                        open_list.append(
                            (simulated, [-direction[0], -direction[1]]))
                        end = time.time()
                if end - start > 10:
                    print(f"Iterations: {self.iterations}")
                    print(f"Open list: {len(open_list)}")
                    start = end
                self.iterations += 1

        print(f"Group ({str(self.group)[1:-1]}) completed.")
        return closed_list

    def visit(self, puzzle: Puzzle, visited_list, closed_list):
        """Checks if permutation with the blank tile has been visited. 
        If not, adds Puzzle without blank tile to closed list with the number of moves made.

        Returns:
            bool: If the permutation has not been visited_list.
        """
        hashed_blank_puzzle = puzzle.hash(self.blank_group)
        if hashed_blank_puzzle in visited_list:
            return False

        visited_list.add(hashed_blank_puzzle)

        hashed_puzzle = puzzle.hash(self.group)
        if hashed_puzzle not in closed_list or closed_list[hashed_puzzle] > puzzle.moves:
            closed_list[hashed_puzzle] = puzzle.moves

        return True

def main():
    """This is the main function of the pattern builder. You can set different groupings
    if you want to. The patterns are independent, so they can be assigned to their own
    processes. This function also stores the pattern data to a file for later use.
    """
    size = 4
    patterns = [PatternBuilder({1,5,6,9,10,13}, size), PatternBuilder({7,8,11,12,14,15}, size),
                PatternBuilder({2,3,4}, size)]
    closed_list = []

    print("Generating patterns, this could take a while...")
    with Pool(processes=3) as pool:
        results = [pool.apply_async(pattern.build_patterns)
                   for pattern in patterns]
        results = [res.get() for res in results]
        closed_list.extend(iter(results))

    with open('patterns.dat', 'wb') as file:
        pickle.dump([x.group for x in patterns], file)
        pickle.dump(closed_list, file)


if __name__ == '__main__':
    main()