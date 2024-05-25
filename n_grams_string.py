from collections import Counter

def find_anagrams(s: str, p: str) -> list:
    """
    Finds all start indices of p's anagrams in s.
    
    Args:
    s (str): The input string.
    p (str): The pattern string whose anagrams are to be found.
    
    Returns:
    list: A list of starting indices of the anagrams.
    
    Example:
    >>> find_anagrams("cbaebabacd", "abc")
    [0, 6]
    """
    p_count = Counter(p)  # Frequency count of characters in p
    s_count = Counter()  # Sliding window frequency count for s
    result = []  # List to store the starting indices of anagrams
    
    p_length = len(p)  # Length of the pattern string
    
    for i in range(len(s)):
        s_count[s[i]] += 1  # Add the current character to the sliding window
        
        if i >= p_length:  # If window size exceeds p_length
            if s_count[s[i - p_length]] == 1:
                del s_count[s[i - p_length]]  # Remove the character out of the window
            else:
                s_count[s[i - p_length]] -= 1  # Decrease the count of the character
        
        if s_count == p_count:  # If the frequency counts match
            result.append(i - p_length + 1)  # Add the start index to the result
    
    return result

# Example usage
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]