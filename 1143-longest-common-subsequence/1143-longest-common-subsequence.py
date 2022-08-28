class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def subsequence(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0 
            if text1[p1] == text2[p2]:
                return subsequence(p1+1, p2+1)+1

            return max(subsequence(p1+1, p2), subsequence(p1, p2+1))
        
        return subsequence(0, 0)
        return res