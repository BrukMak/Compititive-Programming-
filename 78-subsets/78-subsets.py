class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(idx, cur_set):
            if idx >= len(nums):
                res.append(cur_set)
                return 
            
            rec(idx + 1, cur_set + [nums[idx]])
            rec(idx+1, cur_set)
            
        rec(0, [])
        return res 
            