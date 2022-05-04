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