from src.logic.puzzle import Puzzle
import pickle
from collections import deque
from multiprocessing import Pool


class PatternBuilder():
    def __init__(self,  group):
        """Intializes the pattern database builder with Puzzle, sets it numbers without shuffling.
        Sets moves from the starting position to 0, and initializes a new group with the blank tile.

        Args:
            group (dict): the group of numbers of the Puzzle included in this pattern.
        """
        self.puzzle = Puzzle()
        self.puzzle.set_numbers()
        self.puzzle.moves = 0
        self.group = group
        self.blank_group = group.copy()
        self.blank_group.add(0)
        self.visited = set()
        self.closed_list = {}

    def build_patterns(self):
        """The method starts with the solved Puzzle and applies BFS to all possible permutations of the Puzzle
        within the group. It uses a queue to store the current permutation and its previous direction.
        The method checks if the permutation has been visited before, and if not, adds it to the visited set.
        It then simulates the Puzzle to every direction and creates a new permutation only if the moved piece is
        in the group. The move is added to the permutation only if the other moves belong to the same group.

        Returns:
            dict: This is the closed list with all of the permutations of the group.
        """
        open_list = deque()
        open_list.append((self.puzzle, [0, 0]))

        while open_list:
            puzzle, previous = open_list.popleft()
            if self.visit(puzzle):
                for direction in self.puzzle.directions:
                    if direction != previous:
                        simulated = puzzle.simulate(direction)
                        if not simulated:
                            continue
                        if simulated[puzzle.position[0]][puzzle.position[1]] in self.group:
                            simulated.moves = puzzle.moves + 1
                        open_list.append(
                            (simulated, [-direction[0], -direction[1]]))

        print(f"Group ({str(self.group)[1:-1]}) completed.")
        return self.closed_list

    def visit(self, puzzle):
        """Check if this permutation of the Puzzle with the blank tile 
        has already been visited. If not, set hash of the Puzzle without
        the blank tile to the closed list, and give it the value how many
        times the Puzzle has been moved in this Puzzle.

        Args:
            puzzle (Puzzle): This is the permutation of the Puzzle.

        Returns:
            bool: If the permutation has not been visited.
        """
        hashed_blank_puzzle = puzzle.hash(self.blank_group)
        if hashed_blank_puzzle in self.visited:
            return False

        self.visited.add(hashed_blank_puzzle)

        hashed_puzzle = puzzle.hash(self.group)
        if hashed_puzzle not in self.closed_list or self.closed_list[hashed_puzzle] > puzzle.moves:
            self.closed_list[hashed_puzzle] = puzzle.moves

        return True


def main(): 
    """This is the main function of the pattern builder. You can set different groupings if you want to. 
    The patterns are independent, so they can be assigned to their own processes. 
    This function also stores the pattern data to a file for later use.
    """
    patterns = [PatternBuilder({1, 2, 3, 4, 7}), PatternBuilder({5, 6, 9, 10, 13}),
                PatternBuilder({8, 11, 12, 14, 15})]
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
