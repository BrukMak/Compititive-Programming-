class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(st):
            inverted = ""
            for ch in st:
                inverted += str(int(ch) ^ 1)
            return inverted
        
        def binaryStr(n):
            if n == 1:
                return "0"
            s = binaryStr(n-1)
            return s + "1" + invert(s)[::-1]
         
        return binaryStr(n)[k-1]