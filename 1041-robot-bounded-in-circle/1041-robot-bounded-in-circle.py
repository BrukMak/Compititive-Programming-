class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
                    # N, S, E, W
        directions = [1, 0, 0, 0]
        for _ in range(4):
            for inst in instructions:
                if inst == 'G':
                    index = directions.index(1)
                    if index == 0:
                        position[1] += 1
                    elif index == 1:
                        position[1] -= 1
                    elif index == 2:
                        position[0] += 1
                    else:
                        position[0] -= 1
                else:
                    self.changeDir(inst, directions)
            if position == [0, 0]:
                return True
        return False
    
    def changeDir(self, instruction, directions):
        index = directions.index(1)
        if instruction == 'R':
            
            if index == 0:
                # to East 
                directions[0] = 0
                directions[2] = 1
            elif index == 1:
                # to West 
                directions[1] = 0
                directions[3] = 1
            elif index == 2:
                # to South
                directions[2] = 0
                directions[1] = 1
            else:
                # to North
                directions[3] = 0
                directions[0] = 1
        else:
            if index == 0:
                # to West
                directions[0] = 0
                directions[3] = 1
            elif index == 1:
                # to East 
                directions[1] = 0
                directions[2] = 1
            elif index == 2:
                # to North
                directions[2] = 0
                directions[0] = 1
            else:
                # to South
                directions[3] = 0
                directions[1] = 1