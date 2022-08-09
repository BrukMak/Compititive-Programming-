class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod =  10**9 + 7
        lookup = defaultdict(int)
        
        for i in arr:
            cur = 1
            for j in arr:
                if j > i: break
                cur += lookup[i/j] * lookup[j]
            lookup[i] = cur
        return sum(lookup.values()) % mod
        