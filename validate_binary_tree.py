class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    """
    Determines if a binary tree is a valid binary search tree (BST).
    
    Args:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    bool: True if the binary tree is a valid BST, False otherwise.
    
    Example:
    >>> root = TreeNode(2)
    >>> root.left = TreeNode(1)
    >>> root.right = TreeNode(3)
    >>> is_valid_bst(root)
    True
    """
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    
    return validate(root)

# Example usage
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(is_valid_bst(root))  # Output: True