# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA = 0
        lenB = 0
        cur1 = headA
        cur2 = headB
        while cur1:
            lenA += 1
            cur1 = cur1.next
        while cur2:
            lenB += 1
            cur2 = cur2.next
        if lenA > lenB:
            cur1 = headA
            d = lenA - lenB
            while d:
                cur1 = cur1.next
                d -= 1
            cur2 = headB
        elif lenA < lenB:
            cur2 = headB
            d = lenB - lenA
            while d:
                cur2 = cur2.next
                d -= 1
            cur1 = headA
        else:
            cur1 = headA
            cur2 = headB
        while cur1:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
            
        return None