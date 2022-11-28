class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        for w, l in matches:
            if w not in indegree:
                indegree[w] = 0
            indegree[l] += 1
        ans = [[],[]]
        
        for k, v in indegree.items():
            if v == 0:
                ans[0].append(k)
            elif v == 1:
                ans[1].append(k)
                
        ans[0].sort()
        ans[1].sort()
        return ans
            