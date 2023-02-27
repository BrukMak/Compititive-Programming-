class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        # Sort by difference
        tasks.sort(key=lambda x: x[0] - x[1])
        
        result = tasks[0][1]
        curr = tasks[0][1] - tasks[0][0]
        
        for i in range(1, len(tasks)):
            if curr < tasks[i][1]:
                result += tasks[i][1] - curr 
                curr += tasks[i][1] - curr
            curr -= tasks[i][0] 
            
            
        return result