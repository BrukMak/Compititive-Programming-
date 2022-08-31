class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s1, s2 = ["("] * n , [")"] * n
        @lru_cache(None)
        def generator(i1, i2, cur):
            if i1 >= n and i2 >= n:
                return cur
            
            if i1 == i2:
                rop = generator(i1+1, i2, cur +s1[i1])
                if rop: res.append(rop)
            else:
                if i1 < n: 
                    op = generator(i1+1, i2, cur+s1[i1])
                    if op != None: res.append(op)
                if i2 < n: 
                    cl = generator(i1, i2+1, cur+s2[i2])
                    if cl != None: res.append(cl)
        generator(0, 0, "")
        return res