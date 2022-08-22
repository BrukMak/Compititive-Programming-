class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        
        m, f, res = 0, 0, 0
        while m < len(nums):
            if k >= nums[f] - nums[m]:
                res = max(res, m-f+1)
                k -= (nums[f]-nums[m])
                m += 1
            else:
                k += (nums[f] - nums[f+1]) * (m-f-1)
                f += 1
        return res