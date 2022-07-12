class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s1, s2, s3, s4 = 0, 0 , 0 , 0 
        tot = sum(matchsticks)
        side = tot // 4
        
        if tot < 4 or tot % 4 != 0:
            return False
        matchsticks.sort(reverse = True)
        
        @lru_cache(maxsize = None)
        
        def dp(idx, s1, s2, s3, s4):
            if s1 == s2 == s3 == s4 == side:
                return True
            
            if s1 > side or s2 > side or  s3 > side or s4 > side or idx >= len(matchsticks):
                return False
            one = dp(idx+1, s1 + matchsticks[idx], s2, s3, s4,)
            two = dp(idx+1, s1, s2 + matchsticks[idx] , s3, s4,)
            three = dp(idx+1, s1, s2, s3 + matchsticks[idx], s4)
            four = dp(idx+1, s1, s2, s3, s4 + matchsticks[idx])
            
            return one or two or three or four
        return dp(0, s1,s2,s3,s4)
            