class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(list(s))
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1