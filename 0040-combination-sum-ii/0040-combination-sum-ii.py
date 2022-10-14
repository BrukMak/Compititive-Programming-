class Solution:
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        N = len(candidates)
        # vis = set()
        @cache
        def helper(idx, curArr, target):
            if idx >= N:
                curArr = sorted(list(curArr))
                if target == 0:
                    # vis.add(tuple(curArr))
                    ans = curArr.copy()
                    
                    res.add(tuple(ans))
                return
            if target - candidates[idx] >= 0:
                helper(idx + 1, curArr + (candidates[idx],), target - candidates[idx])
            helper(idx + 1, curArr, target)
            
        helper(0, (), target)
        return res