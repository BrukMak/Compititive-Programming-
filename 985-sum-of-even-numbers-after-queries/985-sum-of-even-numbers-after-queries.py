class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        ans = []
        for i in nums:
            if i % 2 == 0:
                evenSum += i
        for q in queries:
            val, idx = q[0], q[1]
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            ans.append(evenSum)
        return ans