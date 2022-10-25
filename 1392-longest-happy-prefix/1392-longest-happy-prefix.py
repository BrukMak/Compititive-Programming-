class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        for i in range(1, len(s)):
            j = lps[i-1]
            while j and s[i] != s[j]:
                j = lps[j-1]
                
            if s[i] == s[j]:
                lps[i] = j + 1                

        # print(lps)
        last_value = lps[-1]
        answer = s[:last_value]
        return answer              
            