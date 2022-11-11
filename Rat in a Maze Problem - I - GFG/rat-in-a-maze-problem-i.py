#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        answer = []
        self.pathFinder(0, 0, [], m, n, answer, set())
        return answer
        
    def inBound(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
        
    def pathFinder(self,row, col, cur_path, grid ,n ,answer, visited):
        if not self.inBound(row, col, n) or grid[row][col] == 0 or (row, col) in visited:
            return
        if row == n - 1 and col == n - 1:
            answer.append("".join(cur_path))
            return
        
        #up
        visited.add((row, col))
        self.pathFinder(row - 1, col, cur_path + ['U'], grid, n, answer, visited)
        visited.remove((row, col))
        #down
        visited.add((row, col))
        self.pathFinder(row + 1, col, cur_path + ['D'], grid, n, answer, visited)
        visited.remove((row, col))
        #left
        visited.add((row, col))
        self.pathFinder(row, col - 1, cur_path + ['L'], grid, n, answer, visited)
        visited.remove((row, col))
        #right
        visited.add((row, col))
        self.pathFinder(row, col + 1, cur_path + ['R'], grid, n, answer, visited)
        visited.remove((row, col))
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends