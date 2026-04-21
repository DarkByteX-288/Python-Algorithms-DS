# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy head to simplify linked list creation
        dummy = ListNode(0)
        current = dummy  # Current position to build result
        
        carry = 0  # Carry from previous addition
        
        # Continue until both lists end AND no carry left
        while l1 or l2 or carry:
            # Get digit values (0 if list ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Add digits + carry
            total = val1 + val2 + carry
            carry = total // 10  # New carry (1 or 0)
            digit = total % 10   # Current digit (0-9)
            
            # Create new node with this digit
            current.next = ListNode(digit)
            current = current.next  # Move to next position
            
            # Move pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return head (skip dummy node)
        return dummy.next