class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def rec(idx, cur_res):
            
            if idx >= len(nums):
                cur_res.sort()
                if cur_res not in res:
                    res.append(cur_res)
                return
            rec(idx+1, cur_res + [nums[idx]])
            rec(idx+1, cur_res)
        
        rec(0, [])
        return res