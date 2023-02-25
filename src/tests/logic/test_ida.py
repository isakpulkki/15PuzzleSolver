import unittest
from src.logic.puzzle import Puzzle
from src.logic.ida import IDAStar


class TestIDAStar(unittest.TestCase):
    def setUp(self):
        puzzle = Puzzle(size=3)
        puzzle.set_numbers()
        simulated = puzzle.simulate([-1, 0])
        self.up, self.right, self.left = (simulated.simulate(x) for x in [
                                          [0, -1], [1, 0], [-1, 0]])
        self.ida_star = IDAStar(simulated)
        group = {1, 2, 3, 4, 5, 6, 7, 8, 0}
        self.ida_star.groups = [group]
        patterns = {self.up.hash(group): 10,
                    self.left.hash(group): 13,
                    self.right.hash(group): 5,
                    simulated.hash(group): 8}
        self.ida_star.patterns = [patterns]

    def test_start_returns_correct_directions(self):
        self.assertEqual(self.ida_star.start(), [[1, 0]])

    def test_heuristic_function_returns_correct_bound(self):
        self.assertEqual(self.ida_star.heuristic(self.right), 5)
        self.assertEqual(self.ida_star.heuristic(self.up), 10)
        self.assertEqual(self.ida_star.heuristic(self.left), 13)
