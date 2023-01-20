class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        
        return self.maxLengthPairs(pairs)
        
    def maxLengthPairs(self, pairs):
        n = len(pairs)
        dp = [1] * (n)
        for i in range(n):
            for j in range(i):
                take = 0
                # take
                if pairs[j][1] < pairs[i][0]:
                    take = dp[j] + 1
                    skip = dp[i]
                    dp[i] = max(take, skip)

        return max(dp)