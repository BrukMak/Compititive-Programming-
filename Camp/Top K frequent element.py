import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        ans = []
        freq = {}
        count = 0
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                 freq[item] = 1
        for key, value in freq.items():
            result.append([-1 * value,key])
        
        heapq.heapify(result)
        
        while count < k:
            ans.append (heapq.heappop(result)[1])
            count += 1
            
        return ans
            
