class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        decStack = []
        for i in nums2:
            while decStack and decStack[-1] <= i:
                nextGreater[decStack.pop()] = i
            decStack.append(i)
        
        while decStack:
            nextGreater[decStack.pop()] = -1
        ans = []
        for i in nums1:
            ans.append(nextGreater[i])
        return ans
            