class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0
        for i in range(len(boxTypes)):
                res += boxTypes[i][1] * min(truckSize, boxTypes[i][0])
                truckSize -= min(truckSize, boxTypes[i][0])
                if truckSize <= 0:
                    break
        return res