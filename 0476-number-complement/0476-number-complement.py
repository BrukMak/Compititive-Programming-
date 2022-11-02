class Solution:
    def findComplement(self, num: int) -> int:
        
        binary_num = bin(num)
        result = []
        for i in binary_num[2:]:
            if int(i):
                result.append('0')
            else:
                result.append('1')
        # print(result)
        return int("".join(result), 2)