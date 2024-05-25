def two_sum(nums: list, target: int) -> list:
    """
    Find two indices in the list `nums` such that the values at those indices sum up to `target`.

    Args:
    nums (List[int]): A list of integers.
    target (int): The target sum.

    Returns:
    List[int]: A list containing the indices of the two numbers that add up to target.

    Raises:
    ValueError: If no two numbers sum up to the target.
    """
    num_to_index = {}  # Initialize an empty dictionary to store number indices
    for i, num in enumerate(nums):  # Iterate over the list with index and value
        complement = target - num  # Calculate the complement that would sum with num to reach target
        if complement in num_to_index:  # Check if the complement is already in the dictionary
            return [num_to_index[complement], i]  # If found, return the indices of complement and current number
        num_to_index[num] = i  # Otherwise, add the current number and its index to the dictionary
    raise ValueError("No two sum solution")  # Raise an error if no valid pairs are found

# Example usage:
nums = [2, 7, 11, 15]  # Define a list of integers
target = 9  # Define the target sum
print(two_sum(nums, target))  # Output: [0, 1] (indices of numbers 2 and 7 that sum up to 9)