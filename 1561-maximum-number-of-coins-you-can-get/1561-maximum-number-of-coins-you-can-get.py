class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        chance = len(piles) // 3
        ptr = -2
        res = 0
        for _ in range(chance):
            res += piles[ptr]
            ptr -= 2
        return res