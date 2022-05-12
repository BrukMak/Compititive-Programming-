class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)[2:][::-1]
        
        itr = 32 - len(n) 
        while itr:
            n += '0'
            itr -= 1
            
        res = int(n, 2)
        
        return res 
        