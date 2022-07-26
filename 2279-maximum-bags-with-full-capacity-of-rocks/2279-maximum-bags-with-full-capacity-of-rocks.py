class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        netCap = []
        for cap, roc in zip(capacity, rocks):
            netCap.append(cap - roc)
        netCap.sort()
        res = 0
        for i in range(len(netCap)):
            if netCap[i] == 0:
                res += 1
            elif netCap[i] > 0:
                toBeSub = min(netCap[i], additionalRocks)
                netCap[i] -= toBeSub
                additionalRocks -= toBeSub
                if netCap[i] == 0: res += 1
            if additionalRocks <= 0:
                break
        return res