class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode with a value and a pointer to the next node.
        
        Args:
        val (int): The value of the node.
        next (ListNode, optional): The next node in the list. Defaults to None.
        """
        self.val = val  # Set the value of the node
        self.next = next  # Set the next node (default is None)

def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists and return it as a new sorted list.
    
    Args:
    l1 (ListNode): The head of the first sorted linked list.
    l2 (ListNode): The head of the second sorted linked list.
    
    Returns:
    ListNode: The head of the merged sorted linked list.
    """
    dummy = ListNode()  # Create a dummy node to act as the head of the merged list
    current = dummy  # Initialize the current pointer to the dummy node

    while l1 and l2:  # Iterate as long as both lists are not empty
        if l1.val < l2.val:  # Compare the values of the nodes in both lists
            current.next = l1  # Attach the smaller node to the current node
            l1 = l1.next  # Move to the next node in list l1
        else:
            current.next = l2  # Attach the smaller or equal node to the current node
            l2 = l2.next  # Move to the next node in list l2
        current = current.next  # Move to the next node in the merged list

    current.next = l1 if l1 else l2  # Attach the remaining nodes of l1 or l2

    return dummy.next  # Return the merged list, starting from the node after the dummy

def print_list(head):
    """
    Print the values in the linked list.
    
    Args:
    head (ListNode): The head of the linked list.
    """
    current = head  # Start with the head node
    while current:  # Iterate through the list
        print(current.val, end=" -> ")  # Print the value of the current node followed by an arrow
        current = current.next  # Move to the next node
    print("None")  # Print the end of the list

# Example usage:
# Creating the first sorted linked list: 1 -> 2 -> 4 -> None
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Creating the second sorted linked list: 1 -> 3 -> 4 -> None
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print("List 1:")
print_list(l1)  # Print the first sorted linked list: 1 -> 2 -> 4 -> None

print("List 2:")
print_list(l2)  # Print the second sorted linked list: 1 -> 3 -> 4 -> None

# Merging the two sorted linked lists
merged_head = merge_two_lists(l1, l2)

print("Merged list:")
print_list(merged_head)  # Print the merged sorted linked list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None