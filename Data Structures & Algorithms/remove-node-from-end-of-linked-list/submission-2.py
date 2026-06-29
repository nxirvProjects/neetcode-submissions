# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        start = dummyNode
        end = dummyNode

        
        # run this loop till n
        for _ in range(n):
            end = end.next
        
        while end.next:
            start = start.next
            end = end.next
            
        
        # Delete the nth node
        start.next = start.next.next

        return dummyNode.next
                
