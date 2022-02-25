class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for row in range(len(grid)):
            l = 0
            r = len(grid[row]) - 1
            while l <= r:
                mid = l + (r - l) // 2
                val = grid[row][mid]
                if  val < 0:
                    count += r - mid + 1
                    r = mid - 1
                    
                else:
                    l = mid + 1
                
                    
        return count
    
