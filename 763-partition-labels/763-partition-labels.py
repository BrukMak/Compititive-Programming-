class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        r = l = sp = 0
        ans = []
        while r < len(s) :
            for i in range(r + 1, len(s)):
                if s[sp] == s[i]:
                    r = i
            if r == l:
                ans.append(1)
                r += 1
                l += 1
                sp = l
                continue
            elif r == len(s) - 1:
                ans.append(r - l + 1)
                break
                
            elif sp == r:
                ans.append(r - l + 1)
                sp += 1
                r += 1
                l = r 
                continue
            sp += 1
        return ans
        