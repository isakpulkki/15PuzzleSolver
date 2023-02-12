# 15PuzzleSolver

This project will be a GUI program that allows users to play the 15 Puzzle game and display optimal moves to solve it by clicking a button. The implementation uses the IDA* algorithm with an additive pattern database as a heuristic to find the optimal path. 

The IDA* algorithm is in its final stages of development and will be integrated into the GUI program shortly. Meanwhile, the pattern builder is completed and is ready for testing.

## Instructions

To run this application, you must have Python3 and Poetry installed. Clone the repository to your preferred location. 

The repository comes with a pre-built additive pattern database that has a grouping of (5, 5, 5), but if you want to customize the groupings, you can easily do so by modifying the code and rebuilding the database.

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

## Documentation

* [Specification](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/specification.md)
* [Testing](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/testing.md)
* [Implementation](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/implementation.md)

## Raports

* [Week 1](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week1.md)
* [Week 2](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week2.md)
* [Week 3](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week3.md)
* [Week 4](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/week4.md)

![CI Badge](https://github.com/isakpulkki/15puzzlesolver/workflows/CI/badge.svg) [![Codecov badge](https://codecov.io/gh/isakpulkki/15PuzzleSolver/branch/main/graph/badge.svg?token=QCJD3KYHM7)](https://codecov.io/gh/isakpulkki/15PuzzleSolver)
