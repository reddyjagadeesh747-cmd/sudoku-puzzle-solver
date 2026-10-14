
# Sudoku Puzzle Solver | Python

## Project Description
A Python-based application that solves 9x9 Sudoku
puzzles using recursion and the backtracking algorithm.

## Technologies Used
- Python
- Recursion
- Backtracking
- Algorithms
- 2D Lists

## Features
- Solves Sudoku puzzles automatically
- Checks valid number placement
- Displays the original and solved grids
- Uses recursive backtracking

## Project Files
- main.py: Main program and grid display
- solver.py: Sudoku solving algorithm
- puzzles.py: Sample Sudoku puzzle

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   python main.py

## Algorithm
The program finds an empty cell and tries numbers
from 1 to 9. If a number violates Sudoku rules,
it tries another number. If a choice leads to a dead
end, backtracking removes that choice and continues
searching for a solution.

## Complexity
Worst-case time complexity: O(9^E), a loose upper
bound, where E is the number of empty cells.
