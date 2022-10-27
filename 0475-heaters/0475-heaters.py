class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        minimum_radius = 0
        for house in houses:
            minimum_radius = max(minimum_radius, self.binarySearch(house, heaters))
        return minimum_radius
    def binarySearch(self, house, heaters):
        l, r = 0, len(heaters) - 1
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, abs(house - heaters[mid]))
            if heaters[mid] == house:
                break
            elif heaters[mid] < house:
                l = mid + 1
            else:
                r = mid - 1
        
        return res

    
    
    