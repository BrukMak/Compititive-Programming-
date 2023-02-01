class Solution:
    def numberOfWays(self, s: str) -> int:

        prefix = [(0,0)]
        sufix = [(0,0)]
        n = len(s)
        
        for i in range(n):
            prev_count_zero = prefix[-1][0]
            prev_count_one = prefix[-1][1]
            if s[i] == '0':
                prefix.append((prev_count_zero + 1, prev_count_one))
            else:
                prefix.append((prev_count_zero, prev_count_one + 1))
        for i in range(n-1, -1, -1):
            prev_count_zero = sufix[-1][0]
            prev_count_one = sufix[-1][1]
            if s[i] == '0':
                sufix.append((prev_count_zero + 1, prev_count_one))
            else:
                sufix.append((prev_count_zero, prev_count_one + 1))
        
        sufix = sufix[::-1]
        answer = 0
        for i in range(1, n - 1):
            if s[i] == '0':
                answer += prefix[i][1] * sufix[i][1]
            else:
                answer += prefix[i][0] * sufix[i][0]
        
        return answer