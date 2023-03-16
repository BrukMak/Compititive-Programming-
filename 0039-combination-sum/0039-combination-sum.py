class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def comb(index, curr, result):
            if sum(curr) == target:
                result.append(curr[:])
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] + sum(curr) > target:
                    break
                comb(i, curr + [candidates[i]], result)
                
        candidates.sort()
        comb(0, [], result)
        return result