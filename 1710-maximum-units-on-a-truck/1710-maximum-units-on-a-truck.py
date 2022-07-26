class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res, ptr = 0, 0
        while ptr < len(boxTypes) and truckSize:
            while ptr < len(boxTypes) and truckSize and boxTypes[ptr][0]:
                res += boxTypes[ptr][1]
                boxTypes[ptr][0] -= 1
                truckSize -= 1
            ptr += 1
        return res