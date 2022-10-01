class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        prod = 1
        for i in nums:
            if i == 0:
                zero += 1
            else:
                prod *= i
        if zero > 1:
            return [0]*len(nums)
        if zero == 1:
            res = [0] * len(nums)
            res[nums.index(0)] = prod
            return res
        res = []
        for num in nums:
            res.append(prod // num)
        return res
        