class Solution:
    def fact(self, num):
        if num == 1:
            return 1
        return num * self.fact(num - 1)
    def countOrders(self, n: int) -> int:
        return (self.fact(2*n) // (2 ** n)) % (10 ** 9 + 7)
            