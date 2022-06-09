# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1, a2 = [], []
        
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        while l2:
            a2.append(l2.val)
            l2 = l2.next
        n1 = len(a1)
        n2 = len(a2)
        if a1[0] + a2[0] >= 10:
            carry = 1
            head = ListNode(a1[0] + a2[0] - 10)
        else:
            carry = 0
            head = ListNode(a1[0] + a2[0])
        
        cur = head
        
        for i in range(1, max(n1, n2)):
            if i < n1 and i < n2:
                if a1[i] + a2[i] + carry >= 10:
                    cur.next = ListNode(a1[i] + a2[i] + carry - 10)
                    carry = 1
                else:
                    cur.next = ListNode(a1[i] + a2[i] + carry)
                    carry = 0
                    
            elif i < n1:
                if a1[i] + carry == 10:
                    
                    cur.next = ListNode(a1[i] + carry - 10)
                    carry = 1
                else:
                    cur.next = ListNode(a1[i] + carry)
                    carry = 0
            else:
                if a2[i] + carry == 10:
                    
                    cur.next = ListNode(a2[i] + carry - 10)
                    carry = 1
                else:
                    cur.next = ListNode(a2[i] + carry)
                    carry = 0
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(carry)
        return head