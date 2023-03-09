class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_level =  self.getRow(rowIndex - 1)
        prev_level.append(0)
        res = []
        for i in range(len(prev_level)):
            res += [prev_level[i]] if i == 0 else [prev_level[i-1] + prev_level[i]]
                
        return res