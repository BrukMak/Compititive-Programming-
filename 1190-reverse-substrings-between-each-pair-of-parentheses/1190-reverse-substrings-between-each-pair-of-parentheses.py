class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] == ")":
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
            else: stack.append(s[i])
            
        return "".join(stack)
            
                
        