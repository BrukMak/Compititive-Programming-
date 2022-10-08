class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def uniqueComb(idx, curArr, tar):
            if idx >= len(candidates):
                if tar == 0:
                    # print(curArr)
                    res.append(curArr.copy())
                return
            if tar - candidates[idx] >= 0:
                uniqueComb(idx, curArr + [candidates[idx]], tar - candidates[idx])
            uniqueComb(idx + 1, curArr, tar)
                        
        uniqueComb(0, [], target)
        return res