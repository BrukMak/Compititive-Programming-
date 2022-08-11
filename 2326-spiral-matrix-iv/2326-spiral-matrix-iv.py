# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1 for i in range(n)]for j in range(m)]
        row, col = 0, 0
        while head:
                    
            while head and col < n and matrix[row][col] == -1:
                matrix[row][col] = head.val
                col += 1
                head = head.next
            row += 1
            col -= 1
            while head and row < m and matrix[row][col] == -1:
                matrix[row][col] = head.val
                row += 1
                head = head.next
            row -= 1
            col -= 1
            while head and col >= 0 and matrix[row][col] == -1:
                matrix[row][col] = head.val
                col -= 1
                head = head.next
            row -= 1
            col += 1
            while head and row >= 0 and matrix[row][col] == -1:
                matrix[row][col] = head.val
                row -= 1
                head = head.next
            col += 1
            row += 1
        return matrix
            
            