class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_pointer = 0
        operations = []
        for current_val in range(1, n+1):
            
            if target[target_pointer] == current_val:
                operations.append('Push')
                target_pointer += 1
            else:
                operations.append('Push')
                operations.append('Pop')

                
            if  target_pointer == len(target):
                break

        return operations