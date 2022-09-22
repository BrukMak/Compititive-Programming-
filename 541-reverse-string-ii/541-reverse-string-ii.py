class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range((len(s) // k)+1):
            if i % 2 == 0:
                res.append(s[:k][::-1])
            else:
                res.append(s[:k])
            s = s[k:]
            
        return "".join(res)