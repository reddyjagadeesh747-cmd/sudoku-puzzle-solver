

def find_best_empty(board):
    best_cell = None
    min_options = 10

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                options = []

                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        options.append(num)

                if len(options) < min_options:
                    min_options = len(options)
                    best_cell = (row, col)

                # No valid number fits this cell
                if min_options == 0:
                    return best_cell

    return best_cell



def is_valid(board, row, col, num):
    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def is_valid_board(board):
    # Check whether the initial puzzle is valid
    for row in range(9):
        for col in range(9):
            num = board[row][col]

            if num == 0:
                continue

            # Temporarily empty the current cell
            board[row][col] = 0

            valid = is_valid(board, row, col, num)

            # Restore the original number
            board[row][col] = num

            if not valid:
                return False

    return True



def solve_sudoku(board):
    empty = find_best_empty(board)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # Backtracking
            board[row][col] = 0

    return False

