class Solution:
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        N = len(candidates)
        candidates.sort()
        @cache
        def helper(idx, curArr, target):
            if idx >= N:
                if target == 0:
                    ans = list(curArr).copy()
                    
                    res.add(tuple(ans))
                return
            if target - candidates[idx] >= 0:
                helper(idx + 1, curArr + (candidates[idx],), target - candidates[idx])
            helper(idx + 1, curArr, target)
            
        helper(0, (), target)
        return res
    
    """
        concatnating to a tuple => (a,b) + (c,)
        reurning set() => could be evaluated as list
        set of tuple could be considered as list of list
        
    """