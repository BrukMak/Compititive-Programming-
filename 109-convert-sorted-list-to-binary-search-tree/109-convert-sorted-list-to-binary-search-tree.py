# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def buildTree(st, e):
            if not st or not e: return
            if st and e and st.val > e.val : return
            if st and e and st.val == e.val: return TreeNode(st.val)
            mid = st
            fast = st
            pre = mid
            while fast and fast.next and fast.val < e.val:
                pre = mid
                mid = mid.next
                fast = fast.next.next
            left = buildTree(st, pre)
            right = buildTree(mid.next, e)
            
            root = TreeNode(mid.val)
            root.left, root.right = left, right
            
            return root
        e = head
        while e and  e.next:
            e = e.next
        return buildTree(head, e)
            