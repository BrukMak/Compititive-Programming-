class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a % b)
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        # Having a range to search for answer
        left = 1
        right = 2 * (10 ** 9 )
        lcm = (divisor1 * divisor2) // self.GCD(divisor1, divisor2)
        ans = right
        
        while left <= right:
            mid = left + (right - left) // 2
            # Have the number of unique values for each array which are valid values
            one = mid - (mid // divisor1)
            two = mid - (mid // divisor2)
            both = mid - (mid // lcm)
            
            if uniqueCnt1 > one or uniqueCnt2 > two or uniqueCnt1 + uniqueCnt2 > both:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1
                
        return ans