class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(st, e):
            if st >= e:
                return 0
            
            return max(piles[st] + dp(st+1, e) , piles[e] + dp(st, e -1))
        return  dp(0, len(piles)-1) > sum(piles) // 2
            