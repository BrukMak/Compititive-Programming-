class Solution:
    def reverseWords(self, s: str) -> str:
        ptr = 0
        ls = []
        while ptr < len(s):
            if s[ptr] != " ":
                mover = ptr
                while mover < len(s):
                    if s[mover] == " ":
                        ls.append(s[ptr:mover])
                        break
                    elif mover == len(s) - 1:
                        ls.append(s[ptr:mover+1])
                    mover += 1
                ptr = mover
            else:
                ptr +=1
        
        outPut = ""
        for i in range(len(ls) - 1,-1,-1):
            outPut +=ls[i]
            if i != 0:
                outPut +=" "
        
        return outPut
