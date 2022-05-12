class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)[2:][::-1]
        
        itr = 32 - len(n) 
        n += "0"*itr
        
        res = int(n, 2)
        
        return res 
        