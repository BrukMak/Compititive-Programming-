class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @cache
#         def helper(pointer1, pointer2):
            
#             if pointer1 >= len(text1) or pointer2 >= len(text2):
#                 return 0
            
#             answer = 0
#             if text1[pointer1] == text2[pointer2]:
#                 return 1 + helper(pointer1 + 1, pointer2 + 1)
#             else:
#                 choice1 = helper(pointer1 + 1, pointer2)
#                 choice2 = helper(pointer1, pointer2 + 1)
                
#                 answer += max(choice1, choice2)
#             return answer
        
#         return helper(0, 0)
        N1 = len(text1)
        N2 = len(text2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        dp[N1][N2] = 0
        
        for pointer1 in range(N1-1, -1, -1):
            for pointer2 in range(N2-1, -1, -1):
                answer = 0
                if text1[pointer1] == text2[pointer2]:
                    answer = 1 + dp[pointer1 + 1][pointer2 + 1]
                else:
                    choice1 = dp[pointer1 + 1][pointer2]
                    choice2 = dp[pointer1][pointer2 + 1]
                
                    answer = max(choice1, choice2)
                dp[pointer1][pointer2] = answer
        return dp[0][0]
        