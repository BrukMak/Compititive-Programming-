class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        toRemove = set()
        for i, char in enumerate(s):
            if not char.isalpha():
                if char == '(':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        toRemove.add(i)
                        
        for i in stack:
            toRemove.add(i)
        res = []
        for i, char in enumerate(s):
            if i not in toRemove:
                res.append(char)
        return "".join(res)
            