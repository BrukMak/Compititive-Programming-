class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = []
        for i in range(1, n+1):
            res.append(bin(i)[2:])
        num = "".join(res)
        num = int(num, 2)
        return num % (10**9 + 7)