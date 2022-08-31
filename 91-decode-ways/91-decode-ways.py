class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if s == "": return 1
        if s[0] == "0": return 0

        one = self.numDecodings(s[1:])
        if len(s) > 1 and int(s[:2]) < 27:
            two = self.numDecodings(s[2:])
            return one + two
        
        return one
