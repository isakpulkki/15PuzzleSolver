# 15PuzzleSolver

This is a Python-based GUI application built with the TKinter library. It enables users to play the 15 Puzzle game and presents them with optimal moves to solve it.

To achieve this, the application employs the Iterative Deepening A* algorithm, which uses an additive pattern database as a heuristic to determine the best moves to solve the puzzle.

## Instructions

To run this application, you must have Python3 and Poetry installed. Clone the repository to your preferred location. 

```bash
# Install dependencies
$ poetry install

# Run the application
$ poetry run invoke start

# Build a new pattern database
$ poetry run invoke build

# Run the tests
$ poetry run invoke test
```

## Hints

To modify the size of the puzzle, adjust the code in [puzzle.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/logic/puzzle.py), but remember to implement an appropriate additive pattern database.

The repository provides a pre-built additive pattern database with a grouping of (5, 5, 5), but you can customize the groupings by modifying the code in [build.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/logic/builder.py) -file and rebuilding the database.

## Documentation

* [Specification](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/specification.md)
* [Testing](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/testing.md)
* [Implementation](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/implementation.md)

## Raports

* [Week 1](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week1.md)
* [Week 2](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week2.md)
* [Week 3](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week3.md)
* [Week 4](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week4.md)
* [Week 5](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week5.md)

![CI Badge](https://github.com/isakpulkki/15puzzlesolver/workflows/CI/badge.svg) [![Codecov badge](https://codecov.io/gh/isakpulkki/15PuzzleSolver/branch/main/graph/badge.svg?token=QCJD3KYHM7)](https://codecov.io/gh/isakpulkki/15PuzzleSolver)
