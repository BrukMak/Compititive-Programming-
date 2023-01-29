class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        status = [False] * len(nums)
        nums.sort()
        unique_permutations = set()
        self.findPermutation(0, nums, unique_permutations)
        
        return unique_permutations
        
    def findPermutation(self, index, nums,unique_permutations):
        if index == len(nums):
            unique_permutations.add(tuple(nums))
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.findPermutation(index + 1, nums, unique_permutations)
            nums[index], nums[i] = nums[i], nums[index]
                