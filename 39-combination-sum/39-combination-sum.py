class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def uniqueComb(idx, curArr, tar):
            if tar < 0: return
            if idx >= len(candidates):
                if tar == 0:
                    # print(curArr)
                    res.append(curArr.copy())
                return
            uniqueComb(idx, curArr + [candidates[idx]], tar - candidates[idx])
            uniqueComb(idx + 1, curArr, tar)
                        
        uniqueComb(0, [], target)
        return res