class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_difference = -1
        increasing_stack = []
        for val in nums:
            while increasing_stack and increasing_stack[-1] >= val:
                increasing_stack.pop()
            if increasing_stack:
                max_difference = max(max_difference, val - increasing_stack[0])
            increasing_stack.append(val)
            
        return max_difference