class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res, ptr = 0, 0
        while ptr < len(boxTypes) and truckSize:
                res += boxTypes[ptr][1] * min(truckSize, boxTypes[ptr][0])
                truckSize -= min(truckSize, boxTypes[ptr][0])
                ptr += 1
        return res