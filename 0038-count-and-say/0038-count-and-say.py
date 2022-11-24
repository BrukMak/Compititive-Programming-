class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(1, n):
            l, r = 0, 0
            temp = []
            while r < len(s):
                flag = False
                while r < len(s) and s[l] == s[r]:
                    flag = True
                    r += 1
                temp.append(str(r-l))
                temp.append(s[l])
                # print(temp, r, l)
                l = r
                if not flag:
                    r += 1
            
            s = "".join(temp)
        return s