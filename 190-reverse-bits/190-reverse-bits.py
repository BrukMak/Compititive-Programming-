class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)[2:][::-1]
        
        itr = 32 - len(n) 
        temp = [n]
        temp.append("0"*itr)
        
        n = "".join(temp)
        
        n = int(n, 2)
        
        return n 
        