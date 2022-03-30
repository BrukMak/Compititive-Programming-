class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        di = defaultdict(int)
        w_size = 0
        left = right = 0
        ans = 0
        while right < len(s):
            di[s[right]] += 1
            cur_max = max(di.values())
            w_size += 1
            while w_size - cur_max > k:
                di[s[left]] -= 1
                left += 1
                w_size -= 1
            
            ans = max(ans, w_size)
            right += 1
        return ans
                
            
        
        