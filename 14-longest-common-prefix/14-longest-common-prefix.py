class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_sized_str = "b" * 300
        for s in strs:
            if len(s) < len(min_sized_str):
                min_sized_str = s
        for i in range(len(min_sized_str)):
            for s in strs:
                if min_sized_str[i] != s[i]:
                    return min_sized_str[:i]
        return min_sized_str
                    