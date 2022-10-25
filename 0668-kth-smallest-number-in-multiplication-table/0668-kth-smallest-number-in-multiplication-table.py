class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        l = 1
        r = m * n
        while r > l:
            mid = l + (r - l) // 2
            res = 0
            for i in range(1, m+1):
                res += min(mid // i, n)
            if res >= k:
                r = mid
            else:
                l = mid + 1
        return l        