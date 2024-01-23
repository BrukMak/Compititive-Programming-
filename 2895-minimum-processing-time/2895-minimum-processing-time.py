class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        proc_per_task = len(tasks) // len(processorTime)
        
        ans = -inf
        
        for i in range(len(processorTime)):
            candidate_index = -(i*proc_per_task + 1)
            ans = max(ans, processorTime[i] + tasks[candidate_index])
            
        return ans