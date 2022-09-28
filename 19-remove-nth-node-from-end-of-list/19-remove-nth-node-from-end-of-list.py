# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        if n == N: return head.next
        cur = head
        ptrStep = N - n - 1
        while ptrStep:
            cur = cur.next
            ptrStep -= 1
        cur.next = cur.next.next
        # if cur.next: cur.next.next = None
        return head
        