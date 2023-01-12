# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resNode = ListNode(0)
        
        def recSum(n1, n2, carry, curNode):
            if not n1 and not n2 and not carry:
                return
            if not n1 and n2:
                curSum = n2.val + carry
                curNode.next = ListNode(curSum % 10)
                recSum(n1, n2.next, curSum // 10, curNode.next)
                
            if not n2 and n1:
                curSum = n1.val + carry
                curNode.next = ListNode(curSum % 10)
                recSum(n1.next, n2, curSum // 10, curNode.next)
                
            if carry and not n1 and not n2:
                curSum = carry
                curNode.next = ListNode(curSum % 10)
                recSum(n1, n2, curSum // 10, curNode.next)
                
            if n1 and n2:
                curSum = n1.val + n2.val + carry
                curNode.next = ListNode(curSum % 10)
                recSum(n1.next, n2.next, curSum // 10, curNode.next)
            return
        cur = resNode
        recSum(l1, l2, 0, cur)
        return resNode.next

        