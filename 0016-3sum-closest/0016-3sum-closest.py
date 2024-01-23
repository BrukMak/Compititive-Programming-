class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = inf
        nums.sort()
        for i in range(len(nums)-1):
            l , r = i + 1, len(nums)-1
            
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                
                if abs(target - cur) < abs(target - best):
                    best = cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return best
                
                
        return best
                
        