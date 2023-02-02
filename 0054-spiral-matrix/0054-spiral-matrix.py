class Solution:
    def spiralOrder(self, inputMatrix: List[List[int]]) -> List[int]:
        # def spiral_copy(inputMatrix):
        n = len(inputMatrix)
        m = len(inputMatrix[0])
        top = 0
        right = len(inputMatrix[0])-1
        bottom = len(inputMatrix)-1
        left = 0
        answer = []

        # def traveler(top, right, bottom, left, inputMatrix):
        # pass



        while len(answer) < n*m:
            #traveler(top, right, bottom, left, inputMatrix)
            # top left to right
            
            for i in range(left, right+1):
                answer.append(inputMatrix[top][i])
            top += 1


            # top right to bottom
            for i in range(top, bottom+1):
                answer.append(inputMatrix[i][right])
            right -= 1


            # right bottom to left
            if top != bottom+1:
                for i in range(right, left-1, -1):
                    answer.append(inputMatrix[bottom][i])
                bottom -= 1


            # left bottom to top
            if right != left-1:
                for i in range(bottom, top-1, -1):
                    answer.append(inputMatrix[i][left])
                left += 1


        return answer