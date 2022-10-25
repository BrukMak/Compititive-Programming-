class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        def dfs(idx, curResult):
            if idx >= len(arr):
                return len(curResult)
            word = arr[idx]
            isFound = False
            for c in word:
                if c in curResult:
                    isFound = True
            take  = 0
            if len(word) == len(set(word)) and not isFound:
                for char in word:
                    curResult.add(char)
                take = dfs(idx + 1, curResult)
                for char in word:
                    curResult.remove(char)
            skip = dfs(idx + 1, curResult)
            
            return max(take, skip)
        return dfs(0, set())
            