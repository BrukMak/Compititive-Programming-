# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val or cur.val-2000 == cur.next.val:
                if cur.val < 1000:
                    cur.val += 2000
                cur.next.val += 2000
                cur = cur.next
            else:
                cur = cur.next
        
        while head and head.val > 1000:
            head = head.next
        
        cur = head
        
        
        while cur and cur.next:
            if cur.next and cur.next.val > 1000:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
            
            
                