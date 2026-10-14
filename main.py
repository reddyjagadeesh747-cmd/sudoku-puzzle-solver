
import time
from copy import deepcopy
from solver import solve_sudoku, is_valid_board
from puzzles import SAMPLE_PUZZLE


def print_board(board):
    print("\n+-------+-------+-------+")

    for row in range(9):
        print("| ", end="")

        for col in range(9):
            value = board[row][col]
            print(value if value != 0 else ".", end=" ")

            if (col + 1) % 3 == 0:
                print("| ", end="")

        print()

        if (row + 1) % 3 == 0:
            print("+-------+-------+-------+")


def get_custom_puzzle():
    board = []

    print("\nEnter 9 rows with 9 numbers per row.")
    print("Use spaces between numbers.")
    print("Enter 0 for empty cells.\n")

    for row in range(9):
        while True:
            try:
                values = list(map(
                    int,
                    input(f"Row {row + 1}: ").split()
                ))

                if len(values) != 9:
                    print("Enter exactly 9 numbers.")
                    continue

                if any(num < 0 or num > 9 for num in values):
                    print("Numbers must be between 0 and 9.")
                    continue

                board.append(values)
                break

            except ValueError:
                print("Invalid input. Enter numbers only.")

    return board


def main():
    print("=" * 35)
    print("       SUDOKU PUZZLE SOLVER")
    print("=" * 35)

    print("1. Solve sample puzzle")
    print("2. Enter your own puzzle")

    choice = input("\nChoose option (1 or 2): ").strip()

    if choice == "1":
        board = deepcopy(SAMPLE_PUZZLE)

    elif choice == "2":
        board = get_custom_puzzle()

    else:
        print("Invalid choice!")
        return

    print("\nOriginal Sudoku:")
    print_board(board)

    if not is_valid_board(board):
        print("\nInvalid Sudoku puzzle!")
        print("Duplicate numbers found in a row, column, or 3x3 box.")
        return

    start_time = time.perf_counter()

    solved = solve_sudoku(board)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if solved:
        print("\nSolved Sudoku:")
        print_board(board)
        print("\nSudoku solved successfully!")
        print(f"Solving time: {elapsed_time:.6f} seconds")
    else:
        print("\nNo solution exists for this puzzle.")
        print(f"Search time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
