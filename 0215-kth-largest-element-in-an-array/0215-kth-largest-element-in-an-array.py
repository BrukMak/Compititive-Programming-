class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        
        for _ in range(k):
            res = -heappop(nums)
        
        return res