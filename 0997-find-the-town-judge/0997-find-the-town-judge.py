class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustee, trusted = defaultdict(int), defaultdict(int)

        for a, b in trust:
            trustee[a] += 1
            trusted[b] += 1
        
        for i in range(1, n+1):
            if trustee[i] == 0 and trusted[i] == n - 1:
                return i
        
        return -1
            