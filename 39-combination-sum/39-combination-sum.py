class Solution:
    def uniqueComb(self, candidates, idx, curArr, tar):
            if idx >= len(candidates):
                if tar == 0:
                    # print(curArr)
                    self.res.append(curArr.copy())
                return
            if tar - candidates[idx] >= 0:
                self.uniqueComb(candidates, idx, curArr + [candidates[idx]], tar - candidates[idx])
            self.uniqueComb(candidates, idx + 1, curArr, tar) 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        
                        
        self.uniqueComb(candidates, 0, [], target)
        return self.res