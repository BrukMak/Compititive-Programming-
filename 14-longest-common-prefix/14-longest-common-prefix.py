class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_sized_str = strs
                
        min_sized_str = min(strs)
        for i in range(len(min_sized_str)):
            for s in strs:
                if min_sized_str[i] != s[i]:
                    return min_sized_str[:i]
        return min_sized_str
                    