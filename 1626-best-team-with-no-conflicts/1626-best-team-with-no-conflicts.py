class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        scores = [s for a,s in sorted(zip(ages, scores))]
        dp = scores.copy()
        ans = 0
        for curr in range(n):
            for prev in range(curr):
                if scores[prev] <= scores[curr]:
                    dp[curr] = max(dp[curr], dp[prev] + scores[curr])
            ans = max(ans, dp[curr])
        return ans