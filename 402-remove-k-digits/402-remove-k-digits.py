class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        mon_stack = []
        if k >= N:
            return "0"
        for n in num:
            while mon_stack and k and mon_stack[-1] > n:
                mon_stack.pop()
                k -= 1
            mon_stack.append(n)
            
        while k > 0:
            mon_stack.pop()
            k -= 1
        return str(int("".join(mon_stack)))