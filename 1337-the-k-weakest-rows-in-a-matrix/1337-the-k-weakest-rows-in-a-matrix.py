class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])
        numOfSoldiers = []
        for row in range(rows):
            numOfSoldiers.append((sum(mat[row]), row))
        numOfSoldiers.sort()
        res = []
        for i in range(k):
            res.append(numOfSoldiers[i][1])
        return res
        
                