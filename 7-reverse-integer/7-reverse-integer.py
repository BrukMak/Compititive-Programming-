class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        else:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            x = int(x) * -1
        if abs(x) > 2**31:
            return 0
        return x
            
        