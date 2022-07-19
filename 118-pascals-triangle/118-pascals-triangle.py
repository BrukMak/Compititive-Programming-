class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        res = [[1]]
        n = 1
        while n < numRows:
            cur = [0]
            cur += res[-1]
            cur.append(0)
            l , r = 0, 1
            ans = []
            while r < len(cur):
                ans.append(cur[l]+cur[r])
                l += 1
                r += 1
            n += 1
            res.append(ans)
        return res