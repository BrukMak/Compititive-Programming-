class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = self.findLPS(s)
        last_value = lps[-1]
        answer = s[:last_value]
        return answer              
        
    def findLPS(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        running = 1
        while running < len(pattern):
            if pattern[running] == pattern[length]:
                lps[running] = length + 1
                running += 1
                length += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    running += 1
        return lps
        
            