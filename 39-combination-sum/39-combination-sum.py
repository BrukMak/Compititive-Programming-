class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        @cache
        def allSum(cur, c_sum, idx):
            if c_sum == target:
                res.append(list(cur))
                return
            if c_sum > target: return
            
            for i in range(idx, N):
                cur = list(cur)
                allSum(tuple(cur + [candidates[i]]), c_sum + candidates[i], i)
        
        allSum((), 0, 0)
        
        return res
                