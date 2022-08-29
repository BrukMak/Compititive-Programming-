class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digComb = defaultdict(list)
        for i in range(30):
            cur = list(str(2 ** i))
            digComb[len(cur)].append(cur)
        nums = list(str(n))
        size = len(nums)
        for lst in digComb[size]:
            for i in range(size):
                if nums[i] in lst:
                    idx = lst.index(nums[i])
                    lst[idx] = '$'
                    if i == size-1: return True
                else: break
        return False