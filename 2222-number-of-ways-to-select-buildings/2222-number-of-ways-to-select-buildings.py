class Solution:
    def numberOfWays(self, s: str) -> int:
#         n = len(s)
#         @lru_cache(maxsize = None)
#         def ways(idx, cur):
#             if idx >= n and len(cur) != 3: return 0
#             if idx >= n and len(cur) == 3: return 1
            
#             if not cur or cur[-1] != s[idx]:
#                 return ways(idx + 1, cur.append(s[idx])) + ways(idx+1, cur)
#             else:
#                 return  ways(idx+1, cur)
        
#         return ways(0, [])

        dp = defaultdict(int)
        for ch in s:
            if ch == '0':
                dp[ch] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            else:
                dp[ch] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
        return dp['101'] + dp['010']