class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def rep(s):
            if s == "": return True
            for i in wordDict:
                if s[:len(i)] == i:
                    if rep(s[len(i):]):
                        return True
            return False
        return rep(s)