class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        pos = self.findPos(xor)
        half1 = 0
        half2 = 0
        for num in nums:
            if num & 1 << pos:
                half1 ^= num
            else:
                half2 ^= num
        return [half1, half2]
    def findPos(self, xor):
        for i in range(32):
            test = xor & 1 << i
            if test:
                return i
