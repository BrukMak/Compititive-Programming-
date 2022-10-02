class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g, p, m = float('-inf'), float('-inf'), float('-inf')
        for i in range(len(garbage)-1, -1, -1):
            if 'G' in garbage[i]: g = max(g, i)
            if 'P' in garbage[i]: p = max(p, i)
            if 'M' in garbage[i]: m = max(m, i)
        cnt = defaultdict(int)
        for ga in garbage:
            for i in ga:
                cnt[i] += 1
        res = sum(list(cnt.values()))
        if g != float('-inf'): res += sum(travel[:g])
        if p != float('-inf'): res += sum(travel[:p]) 
        if m != float('-inf'): res += sum(travel[:m])
        
        return res
                
            