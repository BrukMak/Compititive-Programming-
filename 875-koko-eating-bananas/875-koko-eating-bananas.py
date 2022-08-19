class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 ,  max(piles)
        
        while l <= r:
            mid = l + (r-l) // 2 
            temp = h
            for i in piles:
                temp -= ceil(i / mid)
                
            if temp >= 0:
                r = mid-1
            else:
                l = mid + 1
        return l