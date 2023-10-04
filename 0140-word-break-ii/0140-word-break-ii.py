class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def dp (l, r, cur):
            if r >= len(s) :

                if s[l:r] in wordDict:
                    cur.append(s[l:r])
                    ans.append(" ".join(cur))
                    cur.pop()
                return
            
            if s[l:r] in wordDict:
                dp(r, r, cur + [s[l:r]])
            dp(l, r+1, cur)
        
        dp(0, 0, [])
        return ans