def solve_n_queens(n: int) -> list:
    """
    Solves the N-Queens problem and returns all distinct solutions.
    
    Args:
    n (int): The size of the chessboard (N×N).
    
    Returns:
    list: A list of solutions, each solution is represented by a list of strings.
    
    Example:
    >>> solve_n_queens(4)
    [['.Q..', '...Q', 'Q...', '..Q.'], 
     ['..Q.', 'Q...', '...Q', '.Q..']]
    """
    def backtrack(row: int):
        """
        Uses backtracking to place queens on the board.
        
        Args:
        row (int): The current row to place the queen.
        """
        if row == n:
            # All queens are placed successfully
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Skip if the position is under attack

            # Place the queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            # Move to the next row
            backtrack(row + 1)
            
            # Remove the queen (backtrack)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    # Initialize the board and sets to keep track of attacks
    board = [['.'] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()
    solutions = []
    
    # Start backtracking from the first row
    backtrack(0)
    return solutions

# Example usage
print(solve_n_queens(4))