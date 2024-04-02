class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = defaultdict(str)
        seen = set()
        
        for i in range(len(s)):
            if s[i] in pair:
                if pair[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen:
                    return False
                pair[s[i]] = t[i]
                seen.add(t[i])
        return True