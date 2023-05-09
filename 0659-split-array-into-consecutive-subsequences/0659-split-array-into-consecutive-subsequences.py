class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        prev = defaultdict(list)
        for i in range(len(nums)):
            # print(prev)
            if i == 0:
                heapq.heappush(prev[nums[i]], 1)
            else:
                if (nums[i] - 1) in prev and prev[nums[i]-1]:
                    min_val = heapq.heappop(prev[nums[i]-1])
                    heapq.heappush(prev[nums[i]], min_val + 1)
                else:
                    heapq.heappush(prev[nums[i]], 1)
        for val in prev.values():
            if val and min(val) < 3:
                return False
        return True
        