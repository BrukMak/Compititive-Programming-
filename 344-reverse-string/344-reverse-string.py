class Solution:
    def rev(self, st, e, s):
        if st >= e:
            return
        s[st], s[e] = s[e], s[st]
        self.rev(st+1, e-1, s)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(0, len(s)-1, s)