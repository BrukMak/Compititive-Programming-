class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        l = 0
        maxScore = 0
        for r in range(1, len(values)):
            maxScore = max(maxScore, values[r] + values[l] + (l - r))
            if values[l] + (l - r) < values[r]:
                l = r
        return maxScore