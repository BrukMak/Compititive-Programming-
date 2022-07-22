# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        larger = ListNode(0)
        smaller = ListNode(0)
        headOfLarger = larger
        headOfSmaller = smaller
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
        larger.next = None
        smaller.next = headOfLarger.next
        
        return headOfSmaller.next