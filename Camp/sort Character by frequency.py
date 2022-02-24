from heapq import heappush, heappop, heapify
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        maxheap = []
        s.split()
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        
        
        if len(di) == 1:
            return str(s)
        else:
            for key, val in di.items():
                heappush(maxheap, (-val, key))

            while maxheap:

                temp = heappop(maxheap)
                ans += temp[1]* (-temp[0])
            return ans
