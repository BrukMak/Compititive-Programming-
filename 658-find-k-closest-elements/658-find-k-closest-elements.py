class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dif = []
        for i in arr:
            dif.append((abs(i - x), i))
        dif.sort()
        res = []
        for i in range(k):
            res.append(dif[i][1])
        res.sort()
        return res