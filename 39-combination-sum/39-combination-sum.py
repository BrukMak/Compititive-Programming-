class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def uniqueComb(idx, curSum, curArr):
            if curSum > target: return
            if idx >= len(candidates):
                if curSum == target:
                    # print(curArr)
                    res.append(curArr.copy())
                return
            
            curSum += candidates[idx]
            curArr.append(candidates[idx])
            uniqueComb(idx , curSum , curArr)

            curSum -= candidates[idx]
            curArr.pop()
            uniqueComb(idx + 1, curSum, curArr)
            
        uniqueComb(0, 0, [])
        return res