from collections import deque
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        par = self.kthGrammar(n-1, (k//2 + k%2))
        if par == 1:
            return 0 if k % 2 == 0 else 1
        else:
            return 1 if k % 2 == 0 else 0
    
                        
                    
                
        