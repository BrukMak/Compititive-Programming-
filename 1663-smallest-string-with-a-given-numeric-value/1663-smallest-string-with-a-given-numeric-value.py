class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ""
        stack = []
        if n == k:
            ans = "a"*n
            return ans
        
        while k > 26:
            k -= 26
            n -= 1
            stack.append(26)
            
        if k >= n:
            k -= (n - 1)
            stack.append(k)
            while n-1:
                stack.append(1)
                n -= 1
        else:
            for i in range(1, len(stack) + 1):
                while k < n and stack[-i] > 1:
                    stack[-i] -= 1
                    print(stack[-i])
                    k += 1
                if k < n:
                    continue
                else:
                    while k:
                        stack.append(1)
                        k -= 1
                    break
        
        stack = stack[::-1]
        
        for i in stack:
            ans += chr(i+96)
        return ans