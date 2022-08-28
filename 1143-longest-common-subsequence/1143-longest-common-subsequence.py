class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def subsequence(p1, p2, memo={}):
            if (p1,p2) in memo: return memo[(p1,p2)]
            if p1 >= len(text1) or p2 >= len(text2):
                return 0 
            if text1[p1] == text2[p2]:
                return subsequence(p1+1, p2+1)+1

            memo[(p1,p2)] = max(subsequence(p1+1, p2, memo), subsequence(p1, p2+1, memo))
            return memo[(p1, p2)]
        
        return subsequence(0, 0)
