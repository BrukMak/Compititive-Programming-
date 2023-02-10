class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums_sorted = [0] * (2 * (10 ** 4) + 1) 
        for num in nums:
            nums_sorted[abs(num)] += 1
        ans = []
        for i, num in enumerate(nums_sorted):
            if num:
                for _ in range(num):
                    ans.append(i**2)
        
        return ans