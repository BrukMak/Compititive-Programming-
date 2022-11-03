class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dup_odd = 0
        dup_even = 0
        diff = 0
        count = Counter(words)
        
        for word in words:
            rev_word = word[::-1]
            if word == rev_word:
                if count[word] % 2:
                    dup_odd = max(dup_odd, count[word] * 2)
                    dup_even += ((count[word] - 1) * 2)
                else:
                    dup_even += (count[word]* 2)
            else:
                if rev_word in count:
                    diff += min(count[word], count[rev_word]) * 4
                    
                    del count[rev_word]
            del count[word]
            
        return diff + dup_odd + dup_even - (dup_odd - 2) if dup_odd else diff + dup_even