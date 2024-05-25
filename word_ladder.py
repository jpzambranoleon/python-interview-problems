from collections import deque

def ladder_length(beginWord: str, endWord: str, wordList: list) -> int:
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.
    
    Args:
    beginWord (str): The starting word.
    endWord (str): The ending word.
    wordList (list): The list of allowed words.
    
    Returns:
    int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    
    Example:
    >>> ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    5
    """
    if endWord not in wordList:
        return 0

    wordList = set(wordList)
    queue = deque([(beginWord, 1)])
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == endWord:
            return steps
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, steps + 1))
    
    return 0

# Example usage
print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5