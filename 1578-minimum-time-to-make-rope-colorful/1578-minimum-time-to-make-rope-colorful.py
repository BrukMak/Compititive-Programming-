class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        minTime = 0
        l = 0
        for r in range(N):
            if colors[r] != colors[l]:
                if r - l  > 1:
                    print(neededTime[l:r])
                    minTime += sum(neededTime[l:r]) - max(neededTime[l:r])
                l = r
        if N - l > 1:
             minTime += sum(neededTime[l:N]) - max(neededTime[l:N])
        return minTime