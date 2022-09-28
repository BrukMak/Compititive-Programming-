class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = defaultdict(int)
        _max = 1
        count[cards[0]]+= 1
        i = 0
        j = 0

        ans  = float("inf")

        while j < len(cards):
            while _max >= 2:
                ans  = min(ans,j - i + 1)
                if count[cards[i]] == _max: _max -= 1
                count[cards[i]] -= 1
                i += 1

            j += 1
            if j < len(cards):
                count[cards[j]] += 1
                _max = max(_max,count[cards[j]])

        return ans if ans != float("inf") else -1