class Solution:
    def reverseWords(self, s: str) -> str:
        ans = list(s.split())
        return " ".join(ans[::-1])