class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        s , p , ans = 0, 0, 0
        e = 1
        while s < len(prices):
            if e < len(prices) and prices[p] == prices[e]+1:
                e += 1
                p += 1
            else:
                if e - s == 2: 
                    ans += 1
                else: 
                    ans += ((e - s)*(e - s - 1)) // 2
                s = e
                e += 1
                p = s
        ans += len(prices)
        return ans