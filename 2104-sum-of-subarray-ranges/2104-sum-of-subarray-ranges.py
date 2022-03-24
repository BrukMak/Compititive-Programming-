class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sub_arr_sum = 0
        
        for i in range(len(nums)):
            max_v = nums[i]
            min_v = nums[i]
            
            for j in range(i+1,len(nums)):
                
                if nums[j] > max_v:
                    max_v = nums[j]
                elif nums[j] < min_v:
                    min_v = nums[j]
                sub_arr_sum += (max_v - min_v)
        return sub_arr_sum