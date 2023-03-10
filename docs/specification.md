# Specification Document

The goal of this project is to create a GUI program that allows the user to play the 15 Puzzle game using mouse input and possibility to shuffle the board. Additionally, the program will provide a button to display the optimal moves required to solve the Puzzle with Iterative Deepening A* algorithm using pattern database as heuristics.

I am also capable of programming in Java and can also do the peer reviews for those projects. I am a student for  bachelor’s in computer science. Documentation is done using Markdown.

## Algorithms and Time Complexity

The program will utilize Python and IDA* algorithm with heuristics to discover the optimal solution to the n-puzzle problem. Initially, the heuristic function chosen was Manhattan distance and linear conflicts. However, due to the full pattern database's size for the 15 puzzle, the program will use the additive pattern database. The pattern builder will adopt a double-ended queue and hashmaps for nodes storage.

The worst-case scenario for time complexities of the additive pattern databases and IDA* algorithms should be O(b<sup>d</sup>). The space complexity should be O(bd), where d is the algorithm's depth.

## Sources

* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [Manhattan distance](https://iq.opengenus.org/manhattan-distance/)
* [Pattern databases](https://link.springer.com/chapter/10.1007/978-3-319-05428-5_2)


