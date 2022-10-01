class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right_pr = []
        left_pr = []
        for num in nums:
            if not left_pr:
                left_pr.append(num)
            else:
                left_pr.append(left_pr[-1] * num)
        for num in reversed(nums):
            if not right_pr:
                right_pr.append(num)
            else:
                right_pr.append(right_pr[-1] * num)
        right_pr.reverse()
        res = []
        for i in range(len(nums)):
            if i and i < len(nums)-1 :
                res.append(left_pr[i-1] * right_pr[i+1])
            elif i == 0:
                res.append(right_pr[i+1])
            else:
                res.append(left_pr[i-1])
        return res
        