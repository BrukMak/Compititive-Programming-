class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        removedColor = image[sr][sc]
        
        if removedColor == newColor:
            return image
        
        row = len(image)
        col = len(image[0])
        def dfs(r,c):
            if image[r][c] == removedColor:
                image[r][c] = newColor
                if r >=1 : dfs(r-1,c)
                if r+1 < row: dfs(r+1,c)
                if c >= 1: dfs(r, c - 1)
                if c+1 < col:dfs(r, c+1)
        
        dfs(sr,sc)
        return image
        
