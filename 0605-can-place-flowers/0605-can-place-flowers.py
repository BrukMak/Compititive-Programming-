class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        invalid = set()
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                invalid.add(i-1)
                invalid.add(i+1)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i not in invalid:
                n -= 1
                invalid.add(i+1)
                invalid.add(i-1)
        return n <= 0