class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(st, e):
            if (st, e) in memo:
                return memo[(st, e)]
            if st >= e:
                return 0
            
            memo[(st, e)] = max(piles[st] + dp(st+1, e) , piles[e] + dp(st, e -1))
            return memo[(st, e)]
        return  dp(0, len(piles)-1) > sum(piles) // 2
            