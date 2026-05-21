# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Create the split of list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        second = slow.next # Remember that slow would atp be the middle element of the LL. So slow.next is the first node of the second half. 
        prev = slow.next = None # The pointer toward the first element of second half is now terminated by this statement
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge two halves
        first = head 
        second = prev # the last node we reversed
        
        while second:
            tmp1, tmp2 = first.next, second.next # storing in temp values since we're modifying the links
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        
