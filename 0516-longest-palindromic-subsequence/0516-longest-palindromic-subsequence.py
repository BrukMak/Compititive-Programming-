class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            option1 = option2 = 0
            if s[l] == s[r]:
                option1 = dp(l + 1, r - 1) + 2
            else:
                option2 = max(dp(l, r - 1), dp(l + 1, r ))
            
            return max(option1, option2)
        
        return dp(0, len(s)-1)