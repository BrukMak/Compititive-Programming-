class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        mon_stack = []
        visited = set()
        count_of_letters = Counter(s)
        
        for i in range(len(s)):
            
            if s[i] in visited:
                count_of_letters[s[i]] -= 1
                continue
            
            while mon_stack and count_of_letters[mon_stack[-1]] > 0 and mon_stack[-1] > s[i]:
                temp = mon_stack.pop()
                visited.remove(temp)
                
            mon_stack.append(s[i])
            visited.add(s[i])
            count_of_letters[s[i]] -= 1

        
        return "".join(mon_stack)
        
                
                    