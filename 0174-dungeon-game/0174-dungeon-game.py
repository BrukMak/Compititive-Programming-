class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    dungeon[i][j] = min(0, dungeon[i][j])
                elif i == n-1:
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i][j+1])
                elif j == m-1:
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i+1][j])
                else:
                    
                    dungeon[i][j] = min(0, dungeon[i][j] + max(dungeon[i+1][j], dungeon[i][j+1]))

        return abs(dungeon[0][0]) + 1