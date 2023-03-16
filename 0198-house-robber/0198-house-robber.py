class Solution:
    def rob(self, nums: List[int]) -> int:
#         @cache
#         def selectOptimal(index):
#             if index >= len(nums):
#                 return 0
#             take = nums[index] + selectOptimal(index + 2)
#             skip = selectOptimal(index + 1)
            
#             return max(take, skip)
        
        # return selectOptimal(0)
        n = len(nums)
        dp = [0] * (n + 2)
        i = n - 1
        for  i in range(n-1, -1, -1):
            take = nums[i] + dp[i + 2]
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        return dp[0]
    
    
    """
    td => 
        state index
        transition  = i [0, n]
        base case = index == n
    Bu=>
        transition = [n 0]
        base case 
    
    """
    