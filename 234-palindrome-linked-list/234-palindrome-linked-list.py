# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pre, slow, fast = head, head, head
        
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        
        
        def rev(node):
            if node == pre:
                return pre
            
            newNode = rev(node.next)
            temp = node.next.next if node and node.next and node.next.next else None
                
            node.next.next = node
            
            node.next = temp
            
            return newNode
        
        head = rev(head)
        if fast:
            slow = slow.next
        
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
        