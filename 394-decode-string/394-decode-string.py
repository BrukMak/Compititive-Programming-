class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp_str = ""
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * temp_str)
        
        return "".join(stack)