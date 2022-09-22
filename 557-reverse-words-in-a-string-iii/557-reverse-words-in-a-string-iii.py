class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(string):
            return string[::-1]
        return " ".join(list(map(rev, s.split())))
        