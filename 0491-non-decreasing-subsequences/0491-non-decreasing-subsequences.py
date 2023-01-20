class Solution:
    def __init__(self):
        self.result = set()
        
    def allSubsequence(self, index, nums, current):
        if index == len(nums):
            if len(current) > 1:
                self.result.add(tuple(current[:]))
            return
        # take
        if not current or current[-1] <= nums[index]:
            current.append(nums[index])
            self.allSubsequence(index + 1, nums, current)
            current.pop()
            
        # skip
        self.allSubsequence(index + 1, nums, current)
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.allSubsequence(0, nums, [])
        
        return self.result
    
    