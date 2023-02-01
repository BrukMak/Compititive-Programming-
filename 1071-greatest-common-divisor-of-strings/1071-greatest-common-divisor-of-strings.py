class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller_str = str1 if len(str1) < len(str2) else str2
        ans = ""
        for i in range(1, len(smaller_str)+1):
            spliter = smaller_str[:i]
            test_s1 = "".join(str1.split(spliter))
            test_s2 = "".join(str2.split(spliter))
            if test_s1 == "" and test_s2 == "":
                ans = spliter 
        return ans