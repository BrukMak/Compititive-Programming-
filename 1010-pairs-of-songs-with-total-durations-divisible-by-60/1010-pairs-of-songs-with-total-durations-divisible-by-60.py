class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        seen = defaultdict(int)
        ans = 0
        for t in time:
            if 60 - (t % 60) in seen:
                ans += seen[60 - (t%60)]
            if t%60:
                seen[(t%60)] += 1 
            else:
                seen[60] += 1
        return ans
                 
                