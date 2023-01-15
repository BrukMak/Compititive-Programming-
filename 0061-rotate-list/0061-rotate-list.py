# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_ = 0
        cur = head
        while cur:
            len_ += 1
            cur = cur.next
            
        if not len_: 
            return None
        
        k = k % len_
        
        start = head
        while k:
            end = start
            while end.next.next:
                end = end.next
            new_node = end.next
            new_node.next = start
            start = new_node
            end.next = None
            k -= 1
            
        return start