class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        di = Counter(s)
        for idx, ch in enumerate(s):
            if di[ch] == 1:
                return idx
        return -1
            