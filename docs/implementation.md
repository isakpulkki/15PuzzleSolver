# Implementation Document

This is a Python-based GUI application built with the TKinter library. It enables users to play the 15 Puzzle game and presents them with optimal moves to solve it.

To achieve this, the application uses the Iterative Deepening A* algorithm, which uses an additive pattern database as a heuristic to determine the best moves to solve the puzzle.

## Algorithms and Time Complexity

The program will use the Python programming language and the IDA* algorithm to find the optimal solution to the n-puzzle problem using heuristics. The heuristic function initially considered was Manhattan distance and linear conflicts, but this took too much time to count. I decided to implement pattern database instead. 

Since a full pattern database for the 15 puzzle would be too large when I calculated the permutations it would have, P(15, 15), the program uses the additive pattern database to split the numbers in to groups. 

### Additive Pattern Database

The pattern database algorithm performs breadth-first search on all permutations within a group where the numbers outside the group are the same. The pattern builder uses parallel processing for faster searching, since the permutations are independent of each other. This results in the time to build the database is the number of permutations, P(n, k), where 'n' is the number of tiles, and 'k' is the number of tiles within the largest group, since we can expect smaller groups being completed earlier with parallel processing.

The pattern database builder uses different data structures. A double-ended queue is used for the open node list because the time complexity of popping from the left and appending is O(1). A dictionary and a set are used for the closed and visited lists, respectively, because they allow retrieval of objects in O(1) time through a hash table.

### Iterative Deepening A*

To solve the puzzle, the program uses the iterative deepening A* algorithm. This algorithm uses depth-first search with a depth limit, which is increased on each iteration until the puzzle is solved. The algorithm only stores the depth of each move, saving space. Therefore, the space complexity is O(d), where 'd' is the depth.

In the worst-case scenario, the time complexity is O(b<sup>d</sup>), where 'b' is the branching factor, which is 3 since we have, in the worst case, three branches after the starting position (three tiles to move). However, since the program uses a heuristic function, so this is highly unlikely to occur.

## Sources

* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [Manhattan distance](https://iq.opengenus.org/manhattan-distance/)
* [Pattern databases](https://link.springer.com/chapter/10.1007/978-3-319-05428-5_2)


