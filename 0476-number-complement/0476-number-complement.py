class Solution:
    def findComplement(self, num: int) -> int:
        
        exp = ceil(log((num + 1), 2))
        
        target = (2 ** exp) - 1 
        print((2 ** 31) - 1)
        return num ^ target & ((2 ** 31) - 1)