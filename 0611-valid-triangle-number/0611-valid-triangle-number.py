class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-1, -1, -1):
            r = i - 1
            l = 0
            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    ans += r - l
                    r -= 1
                else:
                    l += 1
                    
        return ans
        
        2