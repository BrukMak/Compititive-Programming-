class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {"2": "abc",
                  "3": "def",
                  "4": "ghi",
                  "5": "jkl",
                  "6": "mno",
                  "7": "pqrs",
                  "8": "tuv",
                  "9": "wxyz"}
        ans = []
        def backtrack(index, curr):
            if index == len(digits):
                if curr:
                    ans.append("".join(curr))
                return
            
            s = mapping[digits[index]]
            for i in range(len(s)):
                backtrack(index + 1, curr + [s[i]])
        backtrack(0, [])
        return ans