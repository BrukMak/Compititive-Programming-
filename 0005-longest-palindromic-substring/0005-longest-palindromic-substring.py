class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.window = s[0]
        for i in range(1,n):
            left, right = i, i
            self.check(left - 1, right, n, s)
            self.check(left, right, n, s)
        return self.window
    
    def check(self, left, right, n, s):
        
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > len(self.window):
                self.window = s[left:right+1]
            left -= 1
            right += 1