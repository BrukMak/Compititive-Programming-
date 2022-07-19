class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        size = len(s)
        rem = ""
        
        for i in range(size):
            
            if s[:size-i] == rev[i:]:
                rem = rev[:i]
                break
        
        s = rem + s
        return s