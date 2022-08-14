class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        
        max_val = len(arr)
        
        for _ in range(len(arr)):
            idx = arr.index(max_val)
            if max_val != idx + 1:
                if idx != 0:
                    res.append(idx + 1)
                    arr[:idx+1] = arr[:idx+1][::-1]
                
                res.append(max_val)
                arr[:max_val] = arr[:max_val][::-1]
            max_val -= 1
        return res