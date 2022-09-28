class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        di = defaultdict(int)
        count = 0
        l = 0
        for i in range(len(s)):
            di[s[i]] += 1
            while len(di) == 3:
                count += len(s) - i
                di[s[l]] -= 1
                if di[s[l]] == 0:
                    di.pop(s[l])
                l += 1
            
        return count