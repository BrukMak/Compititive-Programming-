class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di = Counter(nums)
        
        for key,val in di.items():
            if val != 2:
                return key
        