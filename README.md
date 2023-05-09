# 15PuzzleSolver

![CI Badge](https://github.com/isakpulkki/15puzzlesolver/workflows/CI/badge.svg) [![Codecov badge](https://codecov.io/gh/isakpulkki/15PuzzleSolver/branch/main/graph/badge.svg?token=QCJD3KYHM7)](https://codecov.io/gh/isakpulkki/15PuzzleSolver)

This is a Python-based GUI application built with the TKinter library. It enables users to play the 15 Puzzle and shows them the optimal moves step-by-step to solve it.

To achieve this, the application uses the Iterative Deepening A* algorithm, which uses an additive pattern database as a heuristic function to determine the best moves to solve the Puzzle.

## Instructions

To run this application, you must have Python3 and [Poetry](https://python-poetry.org) installed. Get the zipped file [here](https://github.com/isakpulkki/15PuzzleSolver/releases/tag/1.0) which includes a database with (6, 6, 3) groupings, or clone the repository to your preferred location which has a database with (5, 5, 5) groupings. 

```bash
# Install dependencies
$ poetry install

# Run the application
$ poetry run invoke start

# Rebuild the pattern database
$ poetry run invoke build

# Run the tests
$ poetry run invoke test

# Run the code validators
$ poetry run invoke pylint
```

If you wish, you can customize the database by modifying the code in [builder.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/logic/builder.py) and then rebuilding it. The games Puzzle size can be changed in [app.py](https://github.com/isakpulkki/15PuzzleSolver/blob/main/src/app.py).

## Documentation

* [Specification](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/specification.md)
* [Implementation](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/implementation.md)
* [Testing](https://github.com/isakpulkki/15PuzzleSolver/blob/main/docs/testing.md)


