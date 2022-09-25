class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        count = 0
        if len(s) < 3:
            return 0
        l = 0
        for i in range(3):
            cnt[s[i]] += 1
        for i in range(3, len(s)):
            if len(cnt) == 3:
                count += 1
            cnt[s[i]] += 1
            if cnt[s[l]] > 1:
                cnt[s[l]] -= 1  
            else: cnt.pop(s[l])
            l += 1
        return count if len(cnt) < 3 else count + 1
            