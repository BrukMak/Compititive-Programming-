class Solution:
    def calculate(self, s: str) -> int:
        st1 = []
        st2 = []
        s = s.replace(" ", "")
        pri = {'/': 2, '*': 2, '+':1, '-':1}
        f, p = 0, 0
        while p < len(s):
            if s[p].isdigit():
                p += 1
                
            else:
                st2.append(s[f:p])
                while len(st1) > 0 and pri[st1[-1]] >= pri[s[p]]:
                    st2.append(st1.pop())
                else:
                    st1.append(s[p])
                f = p + 1
                p += 1
                
        st2.append(s[f:p])
        
        while st1:
            st2.append(st1.pop())
        
        for i in st2:
            if i.isdigit(): st1.append(i)
            else:
                num1 = int(st1.pop())
                num2 = int(st1.pop())
                if i == '*':
                    num1 = num2 * num1
                elif i == '/':
                    num1 = num2 // num1
                elif i == '+':
                    num1 = num1 + num2
                else:
                    num1 = num2 - num1
                st1.append(num1)
        return st1[0]