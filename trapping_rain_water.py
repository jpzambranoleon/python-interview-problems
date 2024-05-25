def trap(height: list) -> int:
    """
    Computes how much water can be trapped after raining given an elevation map.
    
    Args:
    height (list): The elevation map.
    
    Returns:
    int: The total amount of trapped water.
    
    Example:
    >>> trap([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
    
    return water_trapped

# Example usage
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6