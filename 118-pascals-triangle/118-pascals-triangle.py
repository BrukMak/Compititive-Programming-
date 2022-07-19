class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        res = [[1]]
        n = 1
        while n < numRows:
            temp = res[-1].copy()
            temp.insert(0,0)
            temp.append(0)
            l , r = 0, 1
            ans = []
            while r < len(temp):
                ans.append(temp[l]+temp[r])
                l += 1
                r += 1
            n += 1
            res.append(ans)
        return res