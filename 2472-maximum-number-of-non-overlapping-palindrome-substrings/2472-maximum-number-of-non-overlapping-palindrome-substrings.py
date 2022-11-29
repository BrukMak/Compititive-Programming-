class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        def isPalindrome(start, end):
            if end > len(s): return False
            return s[start:end] == s[start:end][::-1]
        @cache
        def helper(index):
            if index >= len(s):
                return 0
            ans = helper(index + 1)
            if isPalindrome(index, index + k):
                ans = max(ans, 1 + helper(index + k))
            if isPalindrome(index, index + 1 + k):
                ans = max(ans, 1 + helper(index + 1 + k))
            return ans
        return helper(0)