class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n % 2 == 0:
                half = power(x, n // 2)
                return half * half
            else:
                half = power(x, n // 2)
                return x * half * half
        ans = power(x, abs(n))
        return 1 / ans if n < 0 else ans