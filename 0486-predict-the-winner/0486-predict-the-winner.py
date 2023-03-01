class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        
        def helper(i, j):
            return max(nums[i] + min(helper(i+2, j), helper(i+1, j-1)) , nums[j] + min(helper(i+1,j-1), helper(i, j-2))) if i <= j else 0
    
        return 2 * helper(0, N - 1) >= sum(nums)
    
        
        
        
        