def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The length of the longest substring without repeating characters.
    
    Example:
    >>> length_of_longest_substring("abcabcbb")
    3
    """
    char_index_map = {}
    longest = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        longest = max(longest, end - start + 1)
    
    return longest

# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3