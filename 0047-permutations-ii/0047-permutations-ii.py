class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        unique_permutations = []
        self.findPermutation(nums, Counter(nums), [], unique_permutations)
        
        return unique_permutations
        
    def findPermutation(self, nums, count, current, unique_permutations):
        if len(current) == len(nums):
            unique_permutations.append(current[:])
            return
        for num in count:
            if count[num] > 0: 
                count[num] -=1
                current.append(num)
                self.findPermutation(nums, count, current, unique_permutations)
                count[num] += 1
                current.pop()
                
                