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

def reverse_list(head):
    """
    Reverse a singly linked list.
    
    Args:
    head (ListNode): The head of the singly linked list.
    
    Returns:
    ListNode: The head of the reversed singly linked list.
    """
    prev = None  # Initialize the previous node as None
    current = head  # Start with the head node as the current node
    while current:  # Iterate until the end of the list
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the link: current node points to the previous node
        prev = current  # Move the previous node to the current node
        current = next_node  # Move to the next node in the list
    return prev  # The new head of the reversed list is the previous node

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
# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)  # Create the head node with value 1
head.next = ListNode(2)  # Create the second node with value 2 and link it to the head
head.next.next = ListNode(3)  # Create the third node with value 3 and link it to the second node
head.next.next.next = ListNode(4)  # Create the fourth node with value 4 and link it to the third node
head.next.next.next.next = ListNode(5)  # Create the fifth node with value 5 and link it to the fourth node

print("Original list:")
print_list(head)  # Print the original linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Reversing the linked list
reversed_head = reverse_list(head)  # Reverse the linked list

print("Reversed list:")
print_list(reversed_head)  # Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1 -> None