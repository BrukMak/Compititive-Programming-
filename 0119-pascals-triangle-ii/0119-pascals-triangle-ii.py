class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_level =  self.getRow(rowIndex - 1)
        prev_level.append(0)
        res = []
        for i in range(len(prev_level)):
            if i == 0:
                res.append(prev_level[i])
            else:
                res.append(prev_level[i-1] + prev_level[i])
        return res