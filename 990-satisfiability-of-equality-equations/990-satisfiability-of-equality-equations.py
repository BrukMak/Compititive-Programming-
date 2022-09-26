class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [x for x in range(26)]
        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                parent[b] = a
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        for eq in equations:
            n1, sign, n2 = eq[0], eq[1:3], eq[3]
            if sign == "==":
                union(ord(n1)-97, ord(n2)-97)

        for eq in equations:
            n1, sign, n2 = eq[0], eq[1:3], eq[3]
            if sign == "!=":
                if find(ord(n1)-97) == find(ord(n2)-97): return False
        
        return True
                    