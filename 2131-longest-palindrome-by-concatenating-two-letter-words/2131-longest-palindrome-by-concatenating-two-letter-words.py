class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dup_odd = 0
        ans = 0
        count = Counter(words)
        
        for word in words:
            rev_word = word[::-1]
            if word == rev_word:
                if count[word] % 2:
                    dup_odd = 1
                ans += (count[word] // 2 * 2)
            else:
                if rev_word in count:
                    ans += min(count[word], count[rev_word]) * 2
                    
                    del count[rev_word]
            del count[word]
            
        return (ans + dup_odd) * 2 