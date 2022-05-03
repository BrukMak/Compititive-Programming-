class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = []
        def rotator(row, col):
            while col < cols and matrix[row][col] != "#":
                visited.append(matrix[row][col])
                matrix[row][col] = "#"
                col += 1
            row += 1
            col -= 1
            while row < rows and matrix[row][col] != "#":
                visited.append(matrix[row][col])
                matrix[row][col] = "#"
                row += 1
            row -= 1
            col -= 1
            while col >= 0 and matrix[row][col] != "#":
                visited.append(matrix[row][col])
                matrix[row][col] = "#"
                col -= 1
            row -= 1
            col += 1
            while row >= 0 and matrix[row][col] != "#":
                visited.append(matrix[row][col])
                matrix[row][col] = "#"
                row -= 1
        for row in range(rows):
            for col in range(cols):
                if row == col:
                    rotator(row, col)
        return visited
            