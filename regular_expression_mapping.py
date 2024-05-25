def is_match(s: str, p: str) -> bool:
    """
    Implements regular expression matching with support for '.' and '*'.
    
    Args:
    s (str): The input string.
    p (str): The pattern string.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    
    Example:
    >>> is_match("aa", "a*")
    True
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]  # DP table to store match results
    dp[0][0] = True  # Empty string matches empty pattern
    
    # Initialize the DP table for patterns like "a*", "a*b*", etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]  # Match single character
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Consider zero occurrence
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Consider one or more occurrence
    
    return dp[m][n]

# Example usage
print(is_match("aa", "a*"))  # Output: True