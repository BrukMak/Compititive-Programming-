class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        # Sort by difference
        tasks.sort(key=lambda x: x[0] - x[1])
        
        my_energy = tasks[0][1]
        current_task = tasks[0][1] - tasks[0][0]
        
        for i in range(1, len(tasks)):
            if current_task < tasks[i][1]:
                my_energy += tasks[i][1] - current_task 
                current_task += tasks[i][1] - current_task
            current_task -= tasks[i][0] 
            
            
        return my_energy