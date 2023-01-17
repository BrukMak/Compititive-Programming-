class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            isSwaped = False
            for j in range(1, len(names)):
                if heights[j] > heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                    names[j], names[j-1] = names[j-1], names[j]
                    isSwaped = True
            if not isSwaped:
                break
                
        return names