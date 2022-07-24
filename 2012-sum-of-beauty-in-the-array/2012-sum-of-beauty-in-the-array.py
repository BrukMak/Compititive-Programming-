class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        preMax = [nums[0]]
        postMin = [0]*(len(nums)-1)
        postMin.append(nums[-1])
        for i in range(1, len(nums)):
            preMax.append(max(preMax[i-1], nums[i]))
        for i in range(len(nums)-2, -1, -1):
            postMin[i] = min(postMin[i+1], nums[i])
        res = 0
        for idx in range(1, len(nums)-1):
            if preMax[idx-1] < nums[idx] < postMin[idx+1]:
                res += 2
            elif nums[idx-1] < nums[idx] < nums[idx+1]:
                res += 1
        return res