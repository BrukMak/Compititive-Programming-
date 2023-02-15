class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique_permutations = []
        self.findPermutation(nums, [], unique_permutations)
        
        return unique_permutations
        
    def findPermutation(self, nums, current, unique_permutations):
        if not nums:
            unique_permutations.append(current[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.findPermutation(nums[:i]+nums[i+1:], current, unique_permutations)
            current.pop()

                