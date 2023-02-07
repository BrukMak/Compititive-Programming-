class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
                    #   N,     S,      E,       W
        directions = [[0, 1],[1, 0],[0, -1], [-1, 0]]
        pointer = 0
        for _ in range(4):
            for inst in instructions:
                if inst == 'G':
                    position[0] += directions[pointer][0]
                    position[1] += directions[pointer][1]
                else:
                    pointer = self.changeDir(inst, directions, pointer)
            if position == [0, 0]:
                return True
        return False
    
    def changeDir(self, instruction, directions, p):
        if instruction == 'R':
            p = (p + 1) % 4
        else:
            p = (p - 1) % 4
        return p
            