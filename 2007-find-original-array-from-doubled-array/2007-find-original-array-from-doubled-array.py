class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        cnt = Counter(changed)
        res = []
        for i in changed:
            if cnt[i] > 0: 
                cnt[i] -= 1
                if 2 * i in cnt and cnt[2*i] > 0:
                    cnt[2*i] -= 1
                    res.append(i)
                else:
                    return []
        return res
            
                