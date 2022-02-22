import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        arr = []
        ans = []
        count = 0
        for i in words:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key, value in freq.items():
            arr.append([-1 * value,key])
        heapq.heapify(arr)
        
        while count < k:
            ans.append(heapq.heappop(arr)[1])
            count += 1
        return ans
