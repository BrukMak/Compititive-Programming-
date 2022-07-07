class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        ls1 = len(s1)
        ls2 = len(s2)
        @lru_cache(maxsize = None)
        
        def dp(i , j):
            if i == len(s1) and j == len(s2):
                return True
            
            ch1, ch2 = False, False
            
            if i < ls1 and s1[i] == s3[i+j]:
                ch1 = dp(i+1, j)
            if j < ls2 and s2[j] == s3[i+j]:
                ch2 = dp(i, j+1)
            return ch1 or ch2
        return dp(0, 0)
                
