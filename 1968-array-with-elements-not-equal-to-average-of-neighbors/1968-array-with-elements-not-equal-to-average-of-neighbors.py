class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ptr = 1
        while ptr < len(nums)-1:
            
            nums[ptr], nums[ptr+1] = nums[ptr+1], nums[ptr]
            ptr += 2
        return nums
        
        