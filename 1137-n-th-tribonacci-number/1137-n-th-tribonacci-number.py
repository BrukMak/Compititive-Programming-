class Solution:
    di = {}
    def tribonacci(self, n: int) -> int:

        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1

        if n not in self.di:
            self.di[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.di[n]
    
            