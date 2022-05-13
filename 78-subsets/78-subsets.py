class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            cur_set = []
            mask = list(bin(i)[2:].strip())
            dif = len(nums) - len(mask)
            for j in range(len(mask)-1, -1, -1):
                if mask[j] == '1':
                    cur_set.append(nums[j+dif])
            res.append(cur_set)
        return res
            