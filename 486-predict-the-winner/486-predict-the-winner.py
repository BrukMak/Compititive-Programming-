class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        half = sum(nums) / 2
        memo = {}
        def helper(i, j):
            if i > j:return 0
            if i == j:
                return nums[j]
            if (i,j) not in memo:
                
                op1 = nums[i] + min(helper(i+2, j), helper(i+1, j-1))
                op2 = nums[j] + min(helper(i+1,j-1), helper(i, j-2))
                memo[(i,j)] = max(op1, op2)
            return memo[(i,j)] 
        
        
        
        return helper(0, N - 1) >= half
    
        
        
        
        