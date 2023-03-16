class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def uniqueComb(index, curr, curr_sum):
            if index >= len(candidates):
                if curr_sum == target:
                    self.res.append(curr[:])
                return 
            if curr_sum + candidates[index] <= target:
                curr.append(candidates[index])
                curr_sum += candidates[index]
                uniqueComb(index, curr, curr_sum)
                curr_sum -= candidates[index]
                curr.pop()
            uniqueComb(index+ 1, curr, curr_sum)
        uniqueComb(0, [], 0)
        return self.res