class Solution:
    def findComplement(self, num: int) -> int:
        shift = 0
        res = 0
        while num:
            if not num & 1:
                res |= 1 << shift
            shift += 1
            num = num >> 1
        return res