def is_valid(s: str) -> bool:
    """
    Determine if the input string is a valid combination of parentheses.

    Args:
    s (str): The input string containing just the characters '(', ')', '{', '}', '[' and ']'.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    stack = []  # Initialize an empty stack to store opening parentheses
    mapping = {')': '(', '}': '{', ']': '['}  # Define a mapping of closing to opening parentheses
    
    for char in s:  # Iterate through each character in the input string
        if char in mapping:  # If the character is a closing parenthesis
            top_element = stack.pop() if stack else '#'  # Pop the top element from the stack if it's not empty, otherwise assign '#'
            if mapping[char] != top_element:  # If the corresponding opening parenthesis doesn't match the top element
                return False  # Return False indicating an invalid combination
        else:  # If the character is an opening parenthesis
            stack.append(char)  # Push it onto the stack
    
    return not stack  # If the stack is empty, all parentheses have been matched, otherwise, return False

# Example usage:
s = "()[]{}"  # Define the input string
print(is_valid(s))  # Output: True (the string contains valid combinations of parentheses)