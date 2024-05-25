def solve_sudoku(board: list) -> None:
    """
    Solves the Sudoku puzzle by filling the empty cells in-place.
    
    Args:
    board (list): A 9x9 2D list representing the Sudoku board.
    
    Example:
    >>> board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
    >>> solve_sudoku(board)
    >>> print(board)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    def is_valid(row: int, col: int, num: str) -> bool:
        """
        Checks if placing the number in the specified cell is valid.
        
        Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (str): The number to place in the cell.
        
        Returns:
        bool: True if the placement is valid, False otherwise.
        """
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                return False
        return True

    def solve() -> bool:
        """
        Solves the Sudoku puzzle using backtracking.
        
        Returns:
        bool: True if the puzzle is solved, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(row, col, num):
                            board[row][col] = num  # Place the number
                            if solve():
                                return True  # If solved, return True
                            board[row][col] = '.'  # Backtrack if not solved
                    return False  # If no number is valid, return False
        return True

    solve()

# Example usage
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solve_sudoku(board)
print(board)