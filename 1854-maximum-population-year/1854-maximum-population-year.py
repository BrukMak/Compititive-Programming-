class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        freq = defaultdict(int)
        for interval in logs:
            for year in range(interval[0], interval[1]):
                freq[year] += 1
        ans = logs[0][0]
        for k, v in freq.items():
            if v > freq[ans]:
                ans = k
            elif v == freq[ans]:
                ans = min(k, ans)
        return ans