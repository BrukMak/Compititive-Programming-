class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        children = [0] * k
        result = float('inf')
        def distribute(index):
            nonlocal result
            if index == len(cookies):
                result = min(result, max(children))
                return 
            if max(children) >= result:
                return 
            for i in range(k):
                if result > children[i] + cookies[index]:
                    children[i] += cookies[index]
                    distribute(index + 1)
                    children[i] -= cookies[index]
        cookies.sort()        
        distribute(0)
        
        return result