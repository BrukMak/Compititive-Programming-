class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        score = 0
        
        for _ in range(k):
            cur = -heapq.heappop(nums)
            heapq.heappush(nums, -ceil(cur / 3))
            score += cur
            
        return score