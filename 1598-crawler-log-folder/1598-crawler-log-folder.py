class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        min_operations = 0
        
        for instruction in logs:
            if instruction == "../":
                min_operations -= 1 if min_operations > 0 else 0
            elif instruction == "./": 
                continue
            else: 
                min_operations += 1
                
        return min_operations
                