class Solution:
    def inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def dfs(self, row, col, cur_color, newColor, image):
        Dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if self.inbound(row, col) and image[row][col] == cur_color:
            
            image[row][col] = newColor
            
            for d in Dir:
                self.dfs(row + d[0], col + d[1], cur_color, newColor, image)
        else: return  
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.rows = len(image)
        self.cols = len(image[0])
        
        cur_color = image[sr][sc]
        if newColor == cur_color:
            return image
        else:
            
            self.dfs(sr,sc, cur_color, newColor, image)
        return image