## Testing Document

The functions and methods of the user interface will not undergo testing as TKinter library presents significant challenges in developing effective tests for it. Testing will be performed on the program's logic, which includes the pattern database builder, IDA* algorithm, and the Puzzle class.

### Testing the Puzzle

The following test cases are for the Puzzle class. The tests are implemented using the unittest module.

#### Test Cases for the Puzzle Class

* Test the creation of the right size array
* Test the setting of numbers in the board with the method 
* Test the movement of numbers to the right, left, up and down 
* Test the shuffling of the board
* Test if the Puzzle is solved
* Test the hash function returns a correct hash

### Testing the PatternBuilder 

The following test cases are for the PatternBuilder class, which is in charge of making additive pattern database for different groupings of the numbers using permutation. The tests are implemented using the unittest module.

#### Test Cases for the PatternBuilder

* Test that the visited set is initially empty when visiting a permutation for the first time
* Test that the closed list is initially empty when building patterns
* Test that visiting a permutation that has not been visited before returns True
* Test that visiting a permutation that has been visited before returns False
* Test that building patterns returns a list with the correct length, and correct length of iterations which should be the number of permutations

#### Testing the Time Complexities of the PatternBuilder

The time complexity for building the database should be O(P(n, k)), which is *k*-permutations of *n*. So, for example of 15-Puzzle, *n* will be the size of the Puzzle, which is 4<sup>2</sup> = 16, and *k* is the largest group we are calculating heuristics for. In this example, let's use grouping of (5, 5, 5), so our *k* will be (5 + 1) = 6, since we would visit all the permutations with the blank tile, so we iterate over P(16, 6) permutations per group. The size of the database will be P(16, 5) per group, since we do not need to count the blank space in those.

We can see that the results we got testing the program with different groupings, alternating the parameters in [test_builder.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/tests/logic/test_builder.py), match the time complexity of O(P(n, k)):

| **Puzzle size** | **Group size** | **Permutations**  |  **Database size** |
| --- | --- | --- | --- |
|3<sup>2</sup>| 2 | 504 | 72 |
|3<sup>2</sup>| 3 | 3024 | 504 |
|4<sup>2</sup>| 3 | 43680 | 3360 |
|4<sup>2</sup>| 4 | 43680 | 524160 |

### Testing the IDAStar

The following test cases are for the IDAStar algorithm, which is in charge of recursively finding the optimal path to solve the Puzzle, using additive pattern database as heuristics.

#### Test Cases for the IDAStar Class

* Test that the start function returns a correct list of moves to make to find the goal state
* Test that the heuristic function returns a correct bound from the list of patterns
* Test that, if there is additive pattern database for 15 Puzzle, that it returns a path of 52 moves for a Puzzle with optimal moves of 52 to goal state

#### Testing the Time Complexities of the IDAStar

Testing the time complexity of this algorithm is not trivial, since this algorithm relies on the heuristic evalution function for its time complexity, that the heuristic function is admissible. 

In the absolute worst-case scenario, the time complexity would be O(b<sup>d</sup>). The heuristic function would be unadmissable, and the program would become unusable. 

The algorithm is tested that it can find the shortest-path for the vast majority of the Puzzles in seconds, some examples of the running times:

| **Groupings** | **Depth** | **Time** |
| --- | --- | --- |
| (5, 5, 5) | 47 | 0,32 seconds |
| (5, 5, 5) | 49 | 0,21 seconds |
| (5, 5, 5) | 51 | 0,47 seconds |
| (6, 6, 3) | 53 | 1,21 seconds |
| (5, 5, 5) | 57 | 15,21 seconds |
| (6, 6, 3) | 59 | 3,21 seconds |

The algorithm performs quite well with pattern database with groupings of (5, 5, 5) for most of the easier Puzzles. For the harder Puzzles, the algorithm benefits from having a pattern database with groupings of (6, 6, 3). To solve the hardest Puzzles with up to 80 moves in optimal time, a pattern database of (7, 8) would be needed.



