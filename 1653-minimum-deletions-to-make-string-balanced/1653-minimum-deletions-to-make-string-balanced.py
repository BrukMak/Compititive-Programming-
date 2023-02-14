class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        ans = float('inf')
        prev_b = 0
        next_a = 0
        for c in s: next_a += 1 if c == 'a' else 0
        for i in range(len(s)):
            b_before_me = prev_b
            a_after_me = next_a if s[i] == 'b' else next_a - 1
            ans = min(ans, b_before_me + a_after_me)
            if s[i] == 'a':
                next_a -= 1
            else:
                prev_b += 1
        
        return ans