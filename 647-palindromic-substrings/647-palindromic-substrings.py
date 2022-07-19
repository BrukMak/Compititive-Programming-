class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        size = len(s)
        def isPal(l, r):
            nonlocal res
            while l >= 0 and r < size and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        for i in range(size):
            # for odd numbered palindroms
            l , r = i, i
            isPal(l, r)
            # for even number palindroms
            l, r = i, i + 1
            isPal(l , r)
        return res
                