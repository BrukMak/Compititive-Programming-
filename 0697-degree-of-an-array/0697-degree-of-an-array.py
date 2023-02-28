class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        degree = max(freq.values())
        if degree == 1:
            return 1
        solution = [n for n in freq if freq[n] == degree]
        
        minlen = math.inf
        for n in solution:
            left = nums.index(n)
            right = len(nums) - nums[::-1].index(n)
            minlen = min(minlen, right-left)
        return minlen