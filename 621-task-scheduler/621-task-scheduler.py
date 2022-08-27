class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxCount = max(count.values())
        numOfMax = 0
        for i in count.values():
            numOfMax += 1 if i == maxCount else 0
        res = (maxCount-1) * (n+1) + numOfMax
        return res if res >= len(tasks) else len(tasks)