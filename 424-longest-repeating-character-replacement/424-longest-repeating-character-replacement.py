class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        di = defaultdict(int)
        left = right = 0
        ans = 0
        cur_max = 0
        while right < len(s):
            di[s[right]] += 1
            cur_max = max(cur_max, di[s[right]])            
            while (right - left + 1) - cur_max > k:
                di[s[left]] -= 1
                left += 1
                
            
            ans = max(ans, (right - left + 1))
            right += 1
        return ans
                
            
        
        