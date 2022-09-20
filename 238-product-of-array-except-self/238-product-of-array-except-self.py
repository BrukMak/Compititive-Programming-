class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPr = []
        sufixPr = []
        for i in nums:
            prefixPr.append(i) if not prefixPr else prefixPr.append(prefixPr[-1]*i)
        for i in nums[::-1]:
            sufixPr.append(i) if not sufixPr else sufixPr.append(sufixPr[-1]*i)
        sufixPr = sufixPr[::-1] 
        res = []
        for i in range(len(nums)):
            if i-1 >=0 and i+1 < len(nums):
                res.append(prefixPr[i-1] * sufixPr[i+1])
            elif i-1 >= 0:
                res.append(prefixPr[i-1])
            elif i+1 < len(nums):
                res.append(sufixPr[i+1])
        return res
                