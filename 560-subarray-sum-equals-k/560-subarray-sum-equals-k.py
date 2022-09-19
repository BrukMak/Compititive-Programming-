class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDict = defaultdict(int)
        prefixDict[0] = 1
        count = 0
        for i in range(len(nums)):
            if i-1 >= 0:
                nums[i] += nums[i-1]
            if nums[i]-k in prefixDict:
                count += prefixDict[nums[i]-k]
            prefixDict[nums[i]] += 1
        return count
            
            
                    
            