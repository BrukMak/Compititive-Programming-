class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        def helper(i, j):
            if i > j:
                return 0
            
            return max(nums[i] - helper(i+1, j), nums[j] - helper(i, j-1))            
            
        return helper(0, N - 1) >= 0
    
        
        
        
        