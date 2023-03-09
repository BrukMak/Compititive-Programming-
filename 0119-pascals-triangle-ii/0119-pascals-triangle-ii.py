class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_level = [0] + self.getRow(rowIndex - 1)
        prev_level.append(0)
        res = []
        for i in range(1, len(prev_level)):
            res.append(prev_level[i-1] + prev_level[i])
        return res