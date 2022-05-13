class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        for i in range(2**len(nums)):
            mask = list(bin(i)[2:].strip())
            dif = len(nums)-len(mask)
            cur_res = []
            for j in range(len(mask)-1, -1, -1):
                
                if mask[j] == '1':
                    cur_res.append(nums[j+dif])
            cur_res.sort()
            if cur_res not in res:
                res.append(cur_res)
        return res