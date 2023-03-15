class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        def helper(i, j, p1_sum, p2_sum, turn):
            if i > j:
                return p1_sum >= p2_sum
            
            if turn:
                left = helper(i+1, j, p1_sum + nums[i], p2_sum, not turn)
                right = helper(i, j-1, p1_sum + nums[j], p2_sum, not turn)
                return left or right
            else:
                left = helper(i+1, j, p1_sum , p2_sum + nums[i], not turn)
                right = helper(i, j-1, p1_sum , p2_sum + nums[j], not turn)
                return left and right
                
        return helper(0, N - 1, 0, 0, True)
    
        
        
        
        