# Specification Document

The goal of this project is to create a GUI program that allows the user to play the 15 Puzzle game. The program could display the optimal moves required to solve the Puzzle with Iterative Deepening A* algorithm using additive pattern database as heuristics.

I am also capable of programming in Java and can also do the peer reviews for those projects. I am a student for  bachelor’s in computer science. Documentation is done using Markdown.

## Algorithms and Time Complexity

The program will utilize Python and IDA* algorithm with heuristics to discover the optimal solution to the n-Puzzle problem. Initially, the heuristic function chosen was Manhattan distance and linear conflicts. However, due to the full pattern database's size for the 15 Puzzle, the program will use the additive pattern database. The pattern builder will adopt a double-ended queue and hashmaps for nodes storage.

The worst-case scenario for time complexities of the additive pattern databases and IDA* algorithms should be O(b<sup>d</sup>). The space complexity should be O(bd), where d is the algorithm's depth.

## Sources

* [Additive pattern database heuristics](https://www.semanticscholar.org/paper/Additive-Pattern-Database-Heuristics-Felner-Korf/639eb0e6110ba09eb16bd6c958064ac6fa08b440)
* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [Manhattan distance](https://iq.opengenus.org/manhattan-distance/)


