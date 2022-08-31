class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            ns = bin(num)
            ns = "".join(ns.split('0'))
            return len(ns)-1
        res = []
        for i in range(n+1):
            res.append(count(i))
        return res