class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        prof = []
        tot_sum = 0
        for i in range(len(costs)):
            heappush(prof, (costs[i][1] - costs[i][0], i))
        
        prof.sort(reverse = True)
        
        for i in range(len(costs)):
            if i < (len(costs)/2):
                tot_sum += costs[prof[i][1]][0]
            else:
                tot_sum += costs[prof[i][1]][1]
        return tot_sum