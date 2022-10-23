class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        allNums = set([i for i in range(1, len(nums)+1)])
        
        for i in nums:
            if i in allNums:
                allNums.remove(i)
            else:
                ans = i
        return [ans, allNums.pop()]