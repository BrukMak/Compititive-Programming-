class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        toRight = ["."] * N
        toRight[0] = dominoes[0]
        toLeft = ["."] * N
        toLeft[N - 1] = dominoes[N - 1]
        for i in range(1, N):
            if toRight[i-1] == 'R' and dominoes[i] == '.':
                toRight[i] = 'R'
            else:
                toRight[i] = dominoes[i]
        for i in range(N - 2, -1, -1):
            if toLeft[i+1] == 'L' and dominoes[i] == '.':
                toLeft[i] = 'L'
            else:
                toLeft[i] = dominoes[i]    
        res = []
        i = 0
        while i < N:
            if toRight[i] == 'R' and toLeft[i] == '.':
                res.append('R')
            elif toLeft[i] == 'L' and toRight[i] == '.':
                res.append('L')
            elif toRight[i] == toLeft[i]:
                res.append(toLeft[i])
            else:
                st = i
                count = 0
                while toRight[i] == 'R' and toLeft[i] == 'L':
                    count += 1
                    i += 1
                if count % 2:
                    res += toRight[st:(st + (count // 2))]
                    res.append('.')
                    st += count//2+1
                    res += toLeft[st:(st + (count // 2))]
                else:
                    res += toRight[st:(st + (count // 2))]
                    st += count//2
                    res += toLeft[st:(st + (count // 2))]
                i -= 1
            i += 1
        return "".join(res)