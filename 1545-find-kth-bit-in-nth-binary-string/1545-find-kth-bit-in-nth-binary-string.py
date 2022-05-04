#Recursive
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
    
#Itrative
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n-1):
            ptr = 0
            inverse =  ""
            while ptr < len(s):
                if int(s[ptr]): inverse += "0"
                else: inverse += "1"
                ptr += 1
            s += "1" + inverse[::-1]
        return s[k-1]
