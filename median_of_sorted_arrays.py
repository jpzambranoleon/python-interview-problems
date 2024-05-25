def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    """
    Finds the median of two sorted arrays.
    
    Args:
    nums1 (list): The first sorted array.
    nums2 (list): The second sorted array.
    
    Returns:
    float: The median of the two sorted arrays.
    
    Example:
    >>> find_median_sorted_arrays([1, 3], [2])
    2.0
    """
    combined = sorted(nums1 + nums2)
    length = len(combined)
    
    if length % 2 == 1:
        return float(combined[length // 2])
    else:
        return (combined[length // 2 - 1] + combined[length // 2]) / 2.0

# Example usage
print(find_median_sorted_arrays([1, 3], [2]))  # Output: 2.0
print(find_median_sorted_arrays([1, 2], [3, 4]))  # Output: 2.5