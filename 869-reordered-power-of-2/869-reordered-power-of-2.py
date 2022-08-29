class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        given = sorted(str(n))
        for i in range(30):
            if given == sorted(str(2**i)): return True
        return False