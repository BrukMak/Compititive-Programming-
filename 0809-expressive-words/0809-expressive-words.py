class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def same(word, s):
            if len(word) != len(s): return False
            for i in range(len(word)):
                c1, l1 = word[i]
                c2, l2 = s[i]
                if c1 != c2: return False
                if l1 != l2 and (l1 > l2 or l2 == 2): return False
            return True
        def group(s):
            res = []
            i = 0
            while i < len(s):
                char = s[i]
                l = 1
                while i+l < len(s) and s[i+l] == char: l += 1
                res.append((char,l))
                i += l
            return res


        s = group(s)
        return len([1 for word in words if same(group(word), s)])