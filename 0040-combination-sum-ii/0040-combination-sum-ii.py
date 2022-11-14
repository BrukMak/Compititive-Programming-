class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        candidates.sort()
        def helper(idx, curArr, target):
            if target == 0:
                res.append(curArr[:])
                return

            for i in range(idx, N):
                if idx != i and i > 0 and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                helper(i + 1, curArr + [candidates[i]], target - candidates[i])
            
        helper(0, [],target)
        return res
    
