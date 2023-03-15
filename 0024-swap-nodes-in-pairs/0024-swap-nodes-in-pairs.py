# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr):
            if not curr or not curr.next:
                return curr
            temp = curr.next
            curr.next = helper(temp.next)
            temp.next = curr
            
            return temp
            
        return helper(head)