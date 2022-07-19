class Solution:
    res = ""
    def isPal(self, l, r, s):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(self.res):
                    self.res = s[l:r+1]
                l -= 1
                r += 1
    def longestPalindrome(self, s: str) -> str:
        
        for i in range(len(s)):
            r , l = i, i
            self.isPal(l, r, s)
            
            l, r = i, i+1
            self.isPal(l, r, s)
        
            
        return self.res