class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        ned_pointer = 0
        hay_pointer = 0
        lps = self.lpsFinder(needle)
        while hay_pointer < len(haystack) and ned_pointer < len(needle):
            if haystack[hay_pointer] == needle[ned_pointer]:
                ned_pointer += 1
                hay_pointer += 1
            else:
                if ned_pointer != 0:
                    ned_pointer = lps[ned_pointer - 1]
                else:
                     hay_pointer += 1
                    
            if ned_pointer == len(needle): 
                return hay_pointer - ned_pointer
            
        return -1        
    def lpsFinder(self, pattern):
        i = 0
        j = 1
        lps = [0] * len(pattern)
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i != 0:
                    i = lps[i-1]
                else:
                    j += 1
        return lps
                        
                    