## Testing Document

### Testing the Puzzle

The following test cases are for the Puzzle class. The tests are implemented using the unittest module.

#### Test Cases for the Puzzle Class

* Test the creation of the right size array
* Test the setting of numbers in the board with the method 
* Test the method get_number by checking if it returns the correct number
* Test the movement of numbers to the right, left, up and down 
* Test the shuffling of the board
* Test if the Puzzle is solved

### Testing the PatternBuilder

The following test cases are for the PatternBuilder class, which is in charge of making additive pattern database for different groupings of the numbers using permutation. The tests are implemented using the unittest module.

#### Test Cases for the PatternBuilder Class

* Test that the visited set is initially empty when visiting a permutation for the first time
* Test that the closed list is initially empty when building patterns
* Test that visiting a permutation that has not been visited before returns True
* Test that visiting a permutation that has been visited before returns False
* Test that building patterns returns a list with the correct length

Test cases for other parts of the application will be added to this document as they become available.