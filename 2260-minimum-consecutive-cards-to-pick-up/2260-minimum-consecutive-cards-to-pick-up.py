class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_ = float('inf')
        occ = defaultdict(int)
        for i in range(len(cards)):
            if cards[i] in occ:
                min_ = min(min_, i - occ[cards[i]] + 1)
            occ[cards[i]] = i
        return min_ if min_ < float('inf') else -1