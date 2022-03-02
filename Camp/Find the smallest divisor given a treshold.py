class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        divisor = float('inf')
        r = max(nums)
        
        while l <= r:
            mid = l + (r - l)//2
            sum = 0 
            print(mid)
            for num in nums:
                sum += ceil(num / mid)
            
            if sum > threshold:
                l = mid + 1
            else:
                divisor = min(divisor, mid)
                r = mid - 1
        return divisor
