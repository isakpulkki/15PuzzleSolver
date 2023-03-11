# 15PuzzleSolver

![CI Badge](https://github.com/isakpulkki/15puzzlesolver/workflows/CI/badge.svg) [![Codecov badge](https://codecov.io/gh/isakpulkki/15PuzzleSolver/branch/main/graph/badge.svg?token=QCJD3KYHM7)](https://codecov.io/gh/isakpulkki/15PuzzleSolver)

This is a Python-based GUI application built with the TKinter library. It enables users to play the 15 Puzzle and shows them the optimal moves step-by-step to solve it.

To achieve this, the application uses the Iterative Deepening A* algorithm, which uses an additive pattern database as a heuristic function to determine the best moves to solve the Puzzle.

## Instructions

To run this application, you must have Python3 and Poetry installed. Clone the repository to your preferred location (note that [Git Large File Storage](https://git-lfs.com) extension is needed). 

```bash
# Install dependencies
$ poetry install

# Run the application
$ poetry run invoke start

# Build a new pattern database
$ poetry run invoke build

# Run the tests
$ poetry run invoke test

# Run the code validators
$ poetry run invoke pylint
```

The repository provides a pre-built additive pattern database with groupings of (6, 6, 3). You can customize the database by modifying the code in [build.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/logic/builder.py), and rebuilding the database.

## Documentation

* [Specification](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/specification.md)
* [Implementation](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/implementation.md)
* [Testing](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/testing.md)

## Raports

* [Week 1](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week1.md)
* [Week 2](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week2.md)
* [Week 3](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week3.md)
* [Week 4](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week4.md)
* [Week 5](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week5.md)
* [Week 6](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week6.md)


