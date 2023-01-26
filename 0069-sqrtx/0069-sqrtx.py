class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(x // 2 + 2):
            square = num * num
            if square > x:
                return num - 1
            if square == x:
                return num
            