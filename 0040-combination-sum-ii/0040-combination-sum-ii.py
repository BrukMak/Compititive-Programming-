class Solution:
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        candidates.sort()
        def helper(idx, curArr, target):
            if target == 0:
                res.append(curArr.copy())
                return
            
            for i in range(idx, N):
                if i != idx and candidates[i] == candidates[i-1]:
                    continue #Skip duplicate starting point
                if target < candidates[i]: 
                    break # target is lower than current candidate
                helper(i+1, curArr + [candidates[i]], target - candidates[i])
            
        helper(0, [], target)
        return res
    
