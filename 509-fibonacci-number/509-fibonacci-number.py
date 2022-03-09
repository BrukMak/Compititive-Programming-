class Solution:
    di = {}
    def fib(self, n: int) -> int:
        
        if n == 1 or n == 0:
            return n
        if n not in self.di:
            self.di[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.di[n]
    