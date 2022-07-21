# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        rev = lst[left-1:right][::-1]
        for i in range(left-1, right):
            lst[i] = rev[i-(left-1)]
        
        cur = head
        for i in lst:
            cur.val = i
            cur = cur.next
        return head
        
            