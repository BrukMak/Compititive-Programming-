class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        inc_stack = []
        for num in nums:
            
            if inc_stack and inc_stack[-1] >= num:
                inc_stack = [num]
                
            else:
                inc_stack.append(num)
                res = max(res, len(inc_stack))
            
        return res