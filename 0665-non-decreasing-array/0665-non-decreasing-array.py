class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        running_max = -inf
        forward_operation = 0
        for i in range(len(nums)-1):
            running_max = max(running_max, nums[i])
            if nums[i+1] < running_max:
                forward_operation += 1
                
        running_min = inf
        backward_operation = 0
        for i in range(len(nums)-1, 0, -1):
            running_min = min(running_min, nums[i])
            if nums[i-1] > running_min:
                backward_operation += 1

        return backward_operation <= 1 or forward_operation <= 1