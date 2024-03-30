class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # find the number of unique characters
        total_unique = len(set(s.strip()))
        length = 0
        
        for cur_unique in range(1, total_unique+1):
            l = 0
            freq = defaultdict(int)
            for r in range(len(s)):
                freq[s[r]] += 1
                while len(freq) > cur_unique:
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        del freq[s[l]]
                    l += 1
                if freq and min(freq.values()) >= k:
                    length = max(length, r - l + 1)
                    
        return length
            