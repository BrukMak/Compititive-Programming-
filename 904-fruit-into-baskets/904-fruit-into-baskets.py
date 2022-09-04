class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        res = 0
        vCount = defaultdict(int)
        end = 0
        while end < len(fruits):
            vCount[fruits[end]] += 1
            while len(vCount) > 2:
                vCount[fruits[start]] -= 1
                if  vCount[fruits[start]] == 0:
                    vCount.pop(fruits[start])
                start += 1
                    
            res = max(res, end-start+1)
            end += 1
        return res