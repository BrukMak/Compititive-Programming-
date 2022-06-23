class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 1000
                N -= 1
        nums.sort()
        return N