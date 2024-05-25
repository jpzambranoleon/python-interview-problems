def longest_increasing_path(matrix: list) -> int:
    """
    Finds the length of the longest increasing path in the matrix.
    
    Args:
    matrix (list): A 2D list of integers representing the matrix.
    
    Returns:
    int: The length of the longest increasing path.
    
    Example:
    >>> longest_increasing_path([[9,9,4], [6,6,8], [2,1,1]])
    4
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1] * cols for _ in range(rows)]  # DP table to store the longest path lengths
    
    def dfs(row: int, col: int) -> int:
        """
        Performs depth-first search to find the longest increasing path from (row, col).
        
        Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
        Returns:
        int: The length of the longest increasing path from the cell.
        """
        if dp[row][col] != -1:
            return dp[row][col]  # Return the cached value if already computed
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Four possible directions
        max_length = 1  # The cell itself is a path of length 1
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(new_row, new_col))  # Recursive call to explore further
        
        dp[row][col] = max_length  # Cache the result
        return max_length
    
    return max(dfs(row, col) for row in range(rows) for col in range(cols))

# Example usage
print(longest_increasing_path([[9,9,4], [6,6,8], [2,1,1]]))  # Output: 4