class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        result = []
        
        def comb(index, curr, result):
            if sum(curr) == target:
                result.append(curr[:])
                return
            
            for i in range(index, len(candidates)):
                if i - 1 >= index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + sum(curr) > target:
                    break
                comb(i+1, curr + [candidates[i]], result)
        candidates.sort()
        comb(0, [], result)
        return result