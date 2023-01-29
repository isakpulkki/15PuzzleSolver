import unittest

from puzzle import Puzzle


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle(4)
        self.puzzle.set_numbers()

    def test_puzzle_creates_right_size_array(self):
        test_puzzle = Puzzle(3)
        self.assertEqual(len(test_puzzle.board) * len(test_puzzle.board[0]), 9)
        self.assertEqual(len(self.puzzle.board) *
                         len(self.puzzle.board[0]), 16)

    def test_setting_the_numbers(self):
        self.assertEqual(self.puzzle.board[0][0], 1)
        self.assertEqual(self.puzzle.board[0][1], 2)

    def test_getting_number(self):
        self.assertEqual(self.puzzle.get_number(0, 0), 1)

    def test_moving_numbers_right(self):
        self.puzzle.move_number([0, -1])
        self.assertEqual(self.puzzle.board[3][3], 15)

    def test_moving_numbers_left(self):
        self.puzzle.move_number([0, 1])
        self.assertEqual(self.puzzle.board[3][2], 15)

    def test_moving_numbers_up(self):
        self.puzzle.move_number([-1, 0])
        self.assertEqual(self.puzzle.board[3][3], 12)

    def test_moving_numbers_down(self):
        self.puzzle.move_number([1, 0])
        self.assertEqual(self.puzzle.board[2][3], 12)

    def test_shuffling_board(self):
        test_board = self.puzzle.board[0][:]
        self.puzzle.shuffle_board(999)
        self.assertNotEqual(self.puzzle.board[0], test_board)
