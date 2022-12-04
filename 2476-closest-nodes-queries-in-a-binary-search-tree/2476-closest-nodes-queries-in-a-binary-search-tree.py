# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        answer = []
        for target in queries:
            l, r = 0, len(nums) - 1
            mid_check = 0
            while l <= r:
                mid = l + (r - l) // 2
                mid_check = mid
                if nums[mid] == target:
                    # answer.append([target, target])
                    break
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if nums[mid_check] == target:
                answer.append([target, target])
            elif l == len(nums):
                answer.append([nums[r], -1])
            elif r == -1:
                answer.append([-1, nums[l]])
            else:
                answer.append([nums[r], nums[l]])
        return answer
                
            
            
        return answer

            