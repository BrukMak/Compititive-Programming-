class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        min_heap = []
        digits = []
        for log in logs:
            s_log = log.split()
            if s_log[1].isdigit():
                digits.append(log)
            else:
                heapq.heappush(min_heap, (log[len(s_log[0]) + 1:], s_log[0]))
        result = []
        while min_heap:
            word, identifier = heapq.heappop(min_heap)
            current = identifier +" "+ word
            result.append(current)
        for d in digits:
            result.append(d)
            
        return result