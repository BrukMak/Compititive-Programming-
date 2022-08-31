class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return len("".join(bin(x ^ y).split('0')))-1