class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(t)
        di = Counter(s)
        for i in range(n):
            if di == Counter(t[0:i] + t[i+1:n]):
                return t[i]
        
                    