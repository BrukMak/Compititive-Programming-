class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0
        for num in nums:
            if num > ans and -num in set_nums:
                ans = num
        
        return ans if ans else -1
                
            