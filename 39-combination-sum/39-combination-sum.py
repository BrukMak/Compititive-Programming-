class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        def allSum(cur, c_sum, idx):
            if c_sum == target:
                res.append(cur)
                return
            if c_sum > target: return
            
            for i in range(idx, N):
                allSum(cur + [candidates[i]], c_sum + candidates[i], i)
        
        allSum([], 0, 0)
        
        return res
                