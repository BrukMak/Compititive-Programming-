class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnts = Counter(s)
        res = 0
        maxOdd = 0
        for i in cnts.values():
            if i % 2 == 0:
                res += i
            else:
                if i > 1:
                    res += (i // 2) * 2
                
                maxOdd = 1
        return res+maxOdd