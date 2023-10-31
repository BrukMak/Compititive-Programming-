# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        
        result = ListNode(0)
        dummy = result
        while p1 and p2:
            if p1.val <= p2.val:
                dummy.next = p1
                p1 = p1.next
            else:
                dummy.next = p2
                p2 = p2.next
                
            dummy = dummy.next
            
        while p1 or p2:
            if p1:
                dummy.next = p1
                p1 = p1.next
                
            elif p2:
                dummy.next = p2
                p2 = p2.next
            dummy = dummy.next
        return result.next