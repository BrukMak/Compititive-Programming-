class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        bound = int(sqrt(c))
        for i in range(bound+1):
            
            l, r = i, bound
            while l <= r:
                mid = l + (r - l) // 2
                curVal = i ** 2 + mid ** 2
                if curVal == c:
                    return True
                elif curVal < c:
                    l = mid + 1
                else: r = mid -1
        return False
