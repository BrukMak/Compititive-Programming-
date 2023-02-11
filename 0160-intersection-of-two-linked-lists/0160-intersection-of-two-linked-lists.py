# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        cur1 = headA
        while cur1:
            visited.add(cur1)
            cur1 = cur1.next
            
        cur2 = headB
        while cur2:
            if cur2 in visited: return cur2
            cur2 = cur2.next
            
        return
            