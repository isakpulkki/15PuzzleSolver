# Specification document

This aim of this project is to implement a GUI program, where the user can fill in the slots with numbers for the 15 Puzzle, and then execute it to show theoptimal moves step by step to solve it. 

I am also capable of programming in Java and can also do the peer reviews for those projects. I am a student for  bachelor’s in computer science. 
Documentation is done using Markdown.

## Algorithms and time complexity

The program will use IDA* algorithm to solve the optimal path and the progam wil be programmed by Python. The heuristic function the program should use is Manhattan distance. For data structures, the program could use map for storing the nodes visited and a stack to to manage stages of the recursion.

The programs worst case scenario for time complexity should be O(b<sup>d</sup>), since the algorithm is ultimately doing breadth-first-search and the space should be O(d), where d is the depth the algorithm is on.

## Sources

* [Iterative deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [Manhattan distance](https://iq.opengenus.org/manhattan-distance/)


