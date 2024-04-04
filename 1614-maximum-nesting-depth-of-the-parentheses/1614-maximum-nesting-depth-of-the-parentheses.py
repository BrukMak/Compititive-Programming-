class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        depth = 0
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if stack:
                    stack.pop()
            depth = max(depth, len(stack))
            
        return depth