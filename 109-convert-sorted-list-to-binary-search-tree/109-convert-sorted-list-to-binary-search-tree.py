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
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def buildTree(st, e):
            if st > e: return
            if st == e: return TreeNode(nums[st])
            mid = st + (e- st) // 2
            left = buildTree(st, mid-1)
            right = buildTree(mid+1, e)
            
            root = TreeNode(nums[mid])
            root.left, root.right = left, right
            return root
        
        return buildTree(0, len(nums)-1)
            