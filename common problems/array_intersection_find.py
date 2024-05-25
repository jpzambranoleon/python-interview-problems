def intersection(nums1: list, nums2: list) -> list:
    """
    Find the intersection of two arrays.

    Args:
    nums1 (List[int]): The first list of integers.
    nums2 (List[int]): The second list of integers.

    Returns:
    List[int]: A list of integers that are the intersection of the two input lists.
    """
    set1 = set(nums1)  # Convert the first list to a set to remove duplicates
    set2 = set(nums2)  # Convert the second list to a set to remove duplicates
    return list(set1 & set2)  # Return the intersection of the two sets as a list

# Example usage:
nums1 = [1, 2, 2, 1]  # Define the first list of integers
nums2 = [2, 2]  # Define the second list of integers
print(intersection(nums1, nums2))  # Output: [2] (intersection of nums1 and nums2)