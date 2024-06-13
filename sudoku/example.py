def find_empty_cell(board):
    """Find an empty cell in the Sudoku board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, pos):
    """Check if a number is valid in the given position."""
    # Check row
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty_cell(board)
    if not empty:
        return True  # Solved
    else:
        row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack
    
    return False

def get_possible_digits(board):
    """Get possible digits for each empty cell in the board."""
    possible_digits = [[[] for _ in range(9)] for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        possible_digits[i][j].append(num)
    
    return possible_digits

def print_board(board):
    """Print the Sudoku board."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example board (0 represents an empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the possible digits for each cell before solving
print("Possible digits for each empty cell:")
possible_digits = get_possible_digits(sudoku_board)
for i in range(9):
    for j in range(9):
        if sudoku_board[i][j] == 0:
            print(f"Cell ({i}, {j}): {possible_digits[i][j]}")

# Solve the Sudoku puzzle

# Example board (0 represents an empty cell)
sudoku_board_test_case = [
    [0, 0, 0, 0, 6, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0,0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0]
]

# Print the possible digits for each cell before solving
print("Possible digits for each empty cell:")
possible_digits = get_possible_digits(sudoku_board_test_case)
for i in range(9):
    for j in range(9):
        if sudoku_board_test_case[i][j] == 0:
            print(f"Cell ({i}, {j}): {possible_digits[i][j]}")

# Solve the Sudoku puzzle
solve_sudoku(sudoku_board_test_case)

# Print the solved Sudoku board
print("\nSolved Sudoku board:")
print_board(sudoku_board_test_case)




solve_sudoku(sudoku_board)

# Print the solved Sudoku board
print("\nSolved Sudoku board:")
print_board(sudoku_board)
