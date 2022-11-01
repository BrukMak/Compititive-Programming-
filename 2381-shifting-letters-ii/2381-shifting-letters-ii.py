class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        change_in_value = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction:
                change_in_value[start] += 1
                change_in_value[end + 1] -= 1
            else:
                change_in_value[start] -= 1
                change_in_value[end + 1] += 1
        for i in range(1, len(change_in_value)):
            change_in_value[i] += change_in_value[i - 1]
        # print(change_in_value)
        ans = []
        for i in range(len(s)):
            old = s[i]
            new = chr((((ord(old) - 97) + change_in_value[i]) % 26) + 97) 
            ans.append(new)
        return "".join(ans)
            
            