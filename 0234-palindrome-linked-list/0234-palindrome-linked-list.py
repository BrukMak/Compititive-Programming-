# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(node):
            if not node or not node.next:
                return node
            
            newHead = reverse(node.next)
            node.next.next = node
            node.next = None
            return newHead
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            new_head = reverse(slow.next)
        else:
            new_head = reverse(slow)
        
        while new_head:
            if head.val != new_head.val:
                return False
            else:
                head = head.next
                new_head = new_head.next
                
        return True
        
            