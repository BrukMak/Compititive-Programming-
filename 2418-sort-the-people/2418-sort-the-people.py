class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        max_num = max(heights)
        count = [[] for _ in range(max_num + 1)]
        
        for i in range(len(names)):
            count[heights[i]].append(names[i])
        ans = []
        for i in range(len(count)-1, -1, -1):
            l = count[i]
            while l:
                ans.append(l.pop())
                
        return ans