class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        names_pair = [(heights[i], names[i]) for i in range(len(names))]
        ans = []
        for i in range(len(names_pair)):
            for j in range(1, len(names_pair)):
                if names_pair[j][0] > names_pair[j-1][0]:
                    names_pair[j], names_pair[j-1] = names_pair[j-1], names_pair[j]
        for h, n in names_pair:
            ans.append(n)
        return ans