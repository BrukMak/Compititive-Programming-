class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            
            if stack and ((stack[-1].isupper() and char.islower()) or (char.isupper() and stack[-1].islower())):
                if stack[-1].lower() == char.lower():
                    stack.pop()
                    continue
            stack.append(char)
            
        return "".join(stack)
            