class Solution:
    def numDecodings(self, s: str, memo = {}) -> int:
        if s in memo: return memo[s]
        if s == "": return 1
        if s[0] == "0": return 0

        one = self.numDecodings(s[1:], memo)
        if len(s) > 1 and int(s[:2]) < 27:
            two = self.numDecodings(s[2:], memo)
            memo[s] = one + two
            return memo[s]
        
        memo[s] = one
        return one
