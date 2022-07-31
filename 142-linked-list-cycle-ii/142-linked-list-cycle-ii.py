# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = set()
        idx = 0
        while head:
            if head not in st:
                st.add(head)
                head = head.next
            else:
                break
        if head:
            return head
        return
        
            