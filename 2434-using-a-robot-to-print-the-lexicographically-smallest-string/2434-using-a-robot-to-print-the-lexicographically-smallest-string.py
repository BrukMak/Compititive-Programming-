class Solution:
    def robotWithString(self, s: str) -> str:
        d, stack, ans = Counter(s), [], []

        for ch in s:
            
            d[ch]-= 1
            stack.append(ch)
            if not d[ch]: d.pop(ch)
                
            while d and stack and min(d) >= stack[-1]:
                ans += stack.pop()

        return ''.join(ans + stack[::-1])