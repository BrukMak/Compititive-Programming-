# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        pre =  None
        
        while cur:
            nextN = cur.next
            cur.next = pre
            pre = cur
            cur = nextN
        slow.next = pre
        
        p1 , p2 = head, slow.next
        ans = 0
        while p2:
            ans = max(ans, p1.val + p2.val)
            p2 = p2.next
            p1 = p1.next
        return ans
            