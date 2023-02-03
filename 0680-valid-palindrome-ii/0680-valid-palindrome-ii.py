class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                trial1 = s[left:right]
                trial2 = s[left+1:right+1]
                return trial1 == trial1[::-1] or trial2 == trial2[::-1]
            left += 1
            right -= 1
        return True