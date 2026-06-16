# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Brute Force
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next
        
        rIndex = len(nodes) - n
        if rIndex == 0:
            return head.next
        
        nodes[rIndex-1].next = nodes[rIndex].next
        nodes[rIndex].next = None

        return head