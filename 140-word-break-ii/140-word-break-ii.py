class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def sentence(s, cur):
            if s == "":
                ans.append(" ".join(cur))
            
            for word in wordDict:
                if len(s) >= len(word) and s[:len(word)] == word:
                    sentence(s[len(word):], cur + [word])
                    
        sentence(s, [])
        return ans
    
