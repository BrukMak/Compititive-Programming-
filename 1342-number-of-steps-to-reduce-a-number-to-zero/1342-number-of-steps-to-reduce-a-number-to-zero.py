class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return num
        return num.bit_length() + bin(num).count("1") - 1