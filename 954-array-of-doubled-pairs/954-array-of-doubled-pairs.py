class Solution:
    def doubleFinder(self, ar):
            cnt = Counter(ar)
            for num in ar:
                if cnt[num] > 0:
                    cnt[num] -= 1

                    if num >= 0 and 2 * num not in cnt  or cnt[2*num] ==0:
                        return False
                    cnt[2*num] -= 1

            return True
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        arr.sort(reverse = True)
        narr = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < 0:
                narr.append(arr.pop())
            else: break
                
        return self.doubleFinder(arr[::-1]) and self.doubleFinder(narr[::-1])
        