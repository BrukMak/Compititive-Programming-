# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast,prev = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev == slow:
            return None
        prev.next = slow.next
        return head