class Solution:
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        vis = set()
        @cache
        def helper(idx, curArr, target):
            if idx >= N:
                curArr = sorted(list(curArr))
                if target == 0 and tuple(curArr) not in vis:
                    vis.add(tuple(curArr))
                    res.append(curArr.copy())
                return
            if target - candidates[idx] >= 0:
                helper(idx + 1, curArr + (candidates[idx],), target - candidates[idx])
            helper(idx + 1, curArr, target)
            
        helper(0, (), target)
        return res