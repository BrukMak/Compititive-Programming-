class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        s = list(s)
        res = 0
        for _ in range(n):
            swaped = False
            i = 0
            while i < (n-1):
                if s[i] == '0' and s[i + 1] == '1':
                    s[i], s[i+1] = s[i+1], s[i]
                    swaped = True
                    i += 1
                i += 1
            if swaped:
                res += 1
            else:
                return res
            
            