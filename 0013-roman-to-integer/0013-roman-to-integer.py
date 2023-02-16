class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 
        }
        ans = 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if i < n-1 and dictionary[s[i]] < dictionary[s[i+1]]:
                ans -= dictionary[s[i]]
            else:
                ans += dictionary[s[i]]
        return ans