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

#### Test Cases for the PatternBuilder Class

* Test that the visited set is initially empty when visiting a permutation for the first time
* Test that the closed list is initially empty when building patterns
* Test that visiting a permutation that has not been visited before returns True
* Test that visiting a permutation that has been visited before returns False
* Test that building patterns returns a list with the correct length

### Testing the IDAStar

The following test cases are for the IDAStar algorithm, which is in charge of recursively finding the optimal path to solve the Puzzle, using additive pattern database as heuristics.

#### Test Cases for the IDAStar Class

* Test that the start function returns a correct list of moves to make to find the goal state
* Test that the heuristic function returns a correct bound from the list of patterns