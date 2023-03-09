class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = 0
        n = len(citations)
        right = n
        
        while left <= right:
            mid = (right + left) // 2
            pos = bisect_left(citations, mid)
            if mid <= n - pos:
                left = mid + 1
            else:
                right = mid - 1
                
        return right