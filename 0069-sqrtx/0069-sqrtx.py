class Solution:
    def mySqrt(self, x: int) -> int:
        
        for num in range(2 ** 16):
            square = num * num
            if square > x:
                return num - 1
            if square == x:
                return num
            