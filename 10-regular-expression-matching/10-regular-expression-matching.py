class Solution:
    i = j = 0
    def isMatch(self, s: str, p: str, i=0, j=0,) -> bool:
        
        if j >= len(p) and i >= len(s):
            return True
        if j >= len(p):
            return False
        
        if j+1 < len(p) and p[j+1] == '*':
            bool1 = False
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                bool1 = self.isMatch(s, p, i + 1, j)
            bool2 = self.isMatch( s, p, i, j+2)
            return bool1 or bool2
        else:
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                return self.isMatch(s, p, i+1, j+1)
            return False
        