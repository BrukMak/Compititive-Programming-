class Solution:
    def findComplement(self, num: int) -> int:
        # Shift the given number by one bit and check its least significant bit with 1
        # if 0 meaning we need 1 at that point
        shift = 0
        res = 0
        while num:
            if not num & 1:
                res |= 1 << shift
            shift += 1
            num = num >> 1
        return res