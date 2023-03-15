# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr, prev):
            if not curr:
                return curr
            temp = prev.next
            prev.next = curr
            temp.next = curr.next
            curr.next = temp
            if temp.next:
                helper(temp.next.next , temp)
        dummy = ListNode(0)
        dummy.next = head
        
        if head: helper(head.next, dummy)
        return dummy.next