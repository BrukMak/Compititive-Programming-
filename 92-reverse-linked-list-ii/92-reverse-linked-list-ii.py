# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, cur2 = head, head
        if left == right:
            return head
        if left > 1:
        
            while left > 1:
                prev = cur
                cur = cur.next
                left -= 1
        else: 
            prev = None
        
        while right > 1:
            cur2 = cur2.next
            right -= 1
        last = cur2.next
        def rev(node):
            
            if node == cur2:
                return node
            newHead = rev(node.next)
            node.next.next = node
            node.next = None
            return newHead
        nxt = rev(cur)
        
        if nxt == prev: return head
        if prev: 
            prev.next = nxt
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = last
            return head
        else: 
            cur = nxt
            while cur.next:
                cur = cur.next
            cur.next = last
            return nxt
            