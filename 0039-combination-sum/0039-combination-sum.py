class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def uniqueComb(index, curr_sum, curr):
            if curr_sum == target:
                self.res.append(curr[:])
                return 
            for i in range(index, len(candidates)):
                if candidates[i] + curr_sum > target:
                    break  
                uniqueComb(i, curr_sum + candidates[i], curr + [candidates[i]])
        candidates.sort()
        uniqueComb(0, 0, [])
        return self.res