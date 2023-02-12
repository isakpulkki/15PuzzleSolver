import unittest
from src.logic.pattern_builder import PatternBuilder
class TestPatternBuilder(unittest.TestCase):
    def setUp(self):

        self.pattern_builder = PatternBuilder({1, 2, 3})
    
    def test_visit_initial_visited_set_is_empty(self):
        visited_set = self.pattern_builder.visited
        self.assertEqual(len(visited_set), 0)

    def test_build_patterns_closed_list_is_initially_empty(self):
        closed_list = self.pattern_builder.closed_list
        self.assertEqual(len(closed_list), 0)

    def test_visit_returns_true_when_permutation_has_not_been_visited(self):
        result = self.pattern_builder.visit(self.pattern_builder.puzzle)
        self.assertEqual(result, True)

    def test_visit_returns_false_when_permutation_has_been_visited(self):
        self.pattern_builder.visit(self.pattern_builder.puzzle)
        result = self.pattern_builder.visit(self.pattern_builder.puzzle)
        self.assertEqual(result, False)

    def test_building_patterns_returns_correct_length_list(self):
        result = self.pattern_builder.build_patterns()
        print(result)
        self.assertEqual(len(result), 3360)
