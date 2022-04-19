class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            nxt = questions[i][1] + 1 + i
            if nxt >= len(questions):
                dp[i] = max(questions[i][0], dp[i+1])
            else:
                dp[i] = max(questions[i][0] + dp[nxt], dp[i+1])
                
        return dp[0]
        