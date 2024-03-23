# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast =  head
        slow = head
        
        
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next 
        print(slow.val)
        def rev(node):
            if not node.next:
                return node
            newHead = rev(node.next)
            node.next.next = node
            node.next = None
            return newHead
        
        revHead = rev(slow)
        
        cur = head
        
        while revHead and revHead.next:
            temp1 = cur.next
            cur.next = revHead
            temp2 = revHead.next
            revHead.next = temp1
            revHead = temp2
            cur = cur.next.next
        
        