class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = [[] for _ in range(numRows)]
        res[0].append(s[0])
        n, idx, ptr = len(s), 1, 0
        while idx < n:  
            if ptr == 0:
                ptr += 1
                while idx < n and ptr < numRows:
                    res[ptr].append(s[idx])
                    ptr += 1
                    idx += 1
                ptr -= 1
            if ptr == numRows-1:
                ptr -= 1
                while idx < n and ptr >= 0:
                    res[ptr].append(s[idx])
                    idx += 1
                    ptr -= 1
                ptr += 1
        ans = []
        for i in range(numRows):
            ans += res[i]
            
        return "".join(ans)
                