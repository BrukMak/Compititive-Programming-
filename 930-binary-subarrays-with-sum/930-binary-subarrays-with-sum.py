class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Approach two
        
        # Have a dictionary tha has sum : count, running sum and the count of the sum
        # For each running / prefix sum, check if rSum - goal in dect, if so increament
        # the result by its count
        
        rSum = defaultdict(int)
        rSum[0] = 1
        res, cSum = 0, 0
        
        for num in nums:
            cSum += num
            print(cSum)
            if cSum - goal in rSum:
                res += rSum[cSum - goal]
            rSum[cSum] += 1
        return res
        