class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            temp = palindrome
            if temp[i] != 'a':
                temp = temp[:i] + 'a' + temp[i + 1:]
                if temp != temp[::-1]: 
                    return temp
            elif temp[i] == 'a' and i == len(palindrome) - 1:
                temp = temp[:i] + 'b'
            
        return temp
            
    