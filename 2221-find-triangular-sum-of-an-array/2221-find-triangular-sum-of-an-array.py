class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        while n > 1:
            cur = []
            for i in range(1, len(nums)):
                cur.append((nums[i] + nums[i-1]) % 10)
            nums = cur
            n -= 1
        return nums[0]