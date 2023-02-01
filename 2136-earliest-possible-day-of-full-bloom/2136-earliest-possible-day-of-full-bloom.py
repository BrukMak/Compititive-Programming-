class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_grow = [[g, p] for g, p in sorted(zip(growTime, plantTime), reverse = True)]
        ans = 0
        
        for i in range(len(plant_grow)):
            if i > 0:
                plant_grow[i][1] += plant_grow[i-1][1] 
            g, p = plant_grow[i]
            ans = max(ans, (p + g))
            
        return ans
        