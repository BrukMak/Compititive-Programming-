class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        nums_sorted = [0] * (2 * (10**4) + 1)
        
        offset = - (min(nums)) if min(nums) < 0 else 0
        
        # Counting Sort
        for num in nums:
            nums_sorted[num + offset] = count[num]
            
        
        for i in range(len(nums_sorted)-1, -1, -1):
            val = nums_sorted[i]
            k -= val
            if k <= 0:
                return i - offset
        
        # Time O(N)
        # Space O(N)