# Implementation Document

This is a Python-based GUI application built with the TKinter library. It enables users to play the 15 Puzzle game and presents them with optimal moves to solve it.

To achieve this, the application uses the Iterative Deepening A* algorithm, which uses an additive pattern database as a heuristic to determine the best moves to solve the puzzle.

## Algorithms and Time Complexity

The program will use the Python programming language and the IDA* algorithm to find the optimal solution to the n-puzzle problem using heuristics. The heuristic function initially considered was Manhattan distance and linear conflicts, but this took too much time to count. I decided to implement pattern database instead. 

Since a full pattern database for the 15 puzzle would be too large when I calculated the permutations it would have, which would be factorial of 16 for 15-puzzle, the program uses the static additive pattern database to split the numbers in to groups. 

### Additive Pattern Database

The pattern database algorithm performs breadth-first search algorithm on all permutations within a group where the numbers outside the group are the same. The pattern builder uses parallel processing for faster searching, since the permutations are independent of each other. This results in the time to build the database is the number of permutations, O(P(n, k)), where 'n' is the number of tiles, and 'k' is the number of tiles within the largest group and the blank square. We can also note that we can expect smaller groups being completed earlier with parallel processing.

The pattern database builder uses different data structures. A double-ended queue is used for the open node list because the time complexity of popping from the left and appending is O(1). A dictionary and a set are used for the closed and visited lists, respectively, because they allow retrieval of objects in O(1) time through a hash table.

![Different Statically-partitioned Databases for Fifteen Puzzle](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/images/figure.png)

### Iterative Deepening A*

The program utilizes the iterative deepening A* algorithm to solve the puzzle. This algorithm is designed to traverse graphs and search for the shortest path between a start node and any of a set of designated goal nodes in a weighted graph. To accomplish this task, the algorithm employs a heuristic function that evaluates the remaining cost required to reach the solved state of the Puzzle.

The time complexity of this algorithm is not trivial, since this algorithm relies on the heuristic evalution function for its time complexity, that the heuristic function is admissible. The absolute worst-case scenario with unadmissable heuristic function for time complexity of this algorithm would be O(b<sup>d</sup>). This algorithm shines with this memory-constrained problem, the algorithms worst-case space complexity would be O(bd).

In this case, 'b' would be branching factor which would be on average 3, when excluding the corners of the Puzzle, and 'd' would be the depth of the Puzzle, which would be 80 in the worst case.

## Sources

* [Additive pattern database heuristics](https://www.semanticscholar.org/paper/Additive-Pattern-Database-Heuristics-Felner-Korf/639eb0e6110ba09eb16bd6c958064ac6fa08b440)
* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [Manhattan distance](https://iq.opengenus.org/manhattan-distance/)



