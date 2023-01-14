class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [chr(i) for i in range(97, 123)]
        for i in range(len(s1)):
            self.union(s1[i], s2[i], parent)
            self.find(s1[i], parent)
        
        result = []
        for c in baseStr:
            result.append(self.find(c, parent))
        return "".join(result)
        
    def union(self, a, b, parent):
        x = self.find(a, parent)
        y = self.find(b, parent)
        if x != y:
            parent[ord(max(x, y)) - 97] = min(x, y)
    def find(self, a, parent):
        if parent[ord(a) - 97] == a:
            return a
        parent[ord(a) - 97] = self.find(parent[ord(a) - 97], parent)
        return parent[ord(a) - 97]
    