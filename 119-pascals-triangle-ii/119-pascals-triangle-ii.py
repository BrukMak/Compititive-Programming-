class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        while rowIndex > 0:
            cur = res.copy()
            cur.insert(0,0)
            cur.append(0)
            ans = []
            for i in range(1, len(cur)):
                ans.append(cur[i-1]+cur[i])
            res = ans
            rowIndex -= 1
        return res
            