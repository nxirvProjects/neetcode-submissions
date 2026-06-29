# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prior = None
        current = head

        while current:
            nxt = current.next
            current.next = prior
            prior = current
            current = nxt
        
        return prior # Because Prior will be the head when the list is reversed

